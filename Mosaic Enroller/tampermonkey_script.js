// Failed - doesn't work because elements aren't always loaded

// ==UserScript==
// @name         Auto-enroll mosaic
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://epprd.mcmaster.ca/psp/prepprd/EMPLOYEE/HRMS_LS/c/SA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL
// @grant        none
// ==/UserScript==

// https://epprd.mcmaster.ca/psp/prepprd/EMPLOYEE/HRMS_LS/c/SA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL

(function() {
    'use strict';
    
    /*
    Elements:
    <a name="DERIVED_REGFRM1_SSR_LINK_STARTOVER" id="DERIVED_REGFRM1_SSR_LINK_STARTOVER" ptlinktgt="pt_peoplecode" tabindex="38" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'DERIVED_REGFRM1_SSR_LINK_STARTOVER');" class="SSSBUTTON_CANCELLINK">Add Another Class</a>

    <a name="DERIVED_REGFRM1_SSR_PB_SUBMIT" id="DERIVED_REGFRM1_SSR_PB_SUBMIT" ptlinktgt="pt_peoplecode" tabindex="362" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'DERIVED_REGFRM1_SSR_PB_SUBMIT');" class="SSSBUTTON_CONFIRMLINK">Finish Enrolling</a>

    <a name="DERIVED_REGFRM1_LINK_ADD_ENRL$82$" id="DERIVED_REGFRM1_LINK_ADD_ENRL$82$" ptlinktgt="pt_peoplecode" tabindex="549" onclick="javascript:cancelBubble(event);" href="javascript:submitAction_win0(document.win0,'DERIVED_REGFRM1_LINK_ADD_ENRL$82$');" class="SSSBUTTON_CONFIRMLINK">Proceed to Step 2 of 3</a>
    */

    // javascript:submitAction_win0(document.win0,'DERIVED_REGFRM1_LINK_ADD_ENRL$82$');
    // javascript:submitAction_win0(document.win0,'DERIVED_REGFRM1_SSR_LINK_STARTOVER');
    // javascript:submitAction_win0(document.win0,'DERIVED_REGFRM1_SSR_PB_SUBMIT');
    
    // window.onload and document.addEventListener do not ever fire
    setInterval(function() {
        try {
            document.getElementById("DERIVED_REGFRM1_LINK_ADD_ENRL$82$").click()
        } catch(err) {
            console.log('Error trying to press enroll button!');
        }
    }, 5000);


    setInterval(function() {
        try {
            document.getElementById("DERIVED_REGFRM1_SSR_LINK_STARTOVER").click()

        } catch(err) {
            console.log('Error trying to press enroll button!');
        }
    }, 5000);



    setInterval(function() {
        try {
            document.getElementById("DERIVED_REGFRM1_SSR_PB_SUBMIT").click()
        } catch(err) {
            console.log('Error trying to press enroll button!');
        }

    }, 5000);
    
    console.log('beginning mosaic');

    

}, false);