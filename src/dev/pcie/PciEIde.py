# Copyright (c) 2005-2007 The Regents of The University of Michigan
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors: Nathan Binkert

from m5.SimObject import SimObject
from m5.params import *
from Ide import IdeID, IdeDisk, IdeController

class PciEIdeController(IdeController):
    type = 'PciEIdeController'
    cxx_header = "dev/pcie_ide_ctrl.hh"

    Status = 0x290        # 0x0280 | 0x0010 Enable Capabilities List
    CapabilityPtr = 0xE8  # Pointer to MSICAP

    # MSICAP - Message Signaled Interrupt Capability
    MSICAPBaseOffset     = 0xE8        # Base offset of MSICAP in PCI Config space
    MSICAPNextCapability = 0x00        # Next capability block: NULL
    MSICAPCapId          = 0x05        # MSI Capability
    MSICAPMsgCtrl        = 0x0000      # MSI Message Control: 32-bit only
                                       #                      1-message
    MSICAPMsgAddr        = 0x00000000  # MSI Message Address
    MSICAPMsgUpperAddr   = 0x00000000  # MSI Message Upper Address
    MSICAPMsgData        = 0x0000      # MSI Message Data
    MSICAPMaskBits       = 0x00000000  # MSI Interrupt Mask Bits
    MSICAPPendingBits    = 0x00000000  # MSI Pending Bits

