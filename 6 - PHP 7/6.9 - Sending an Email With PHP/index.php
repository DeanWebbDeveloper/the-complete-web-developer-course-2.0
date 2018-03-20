<?php

    $emailTo = "dean@deanwebbdeveloper.com";

    $subject = "Email Test";

    $body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent
            interdum tristique suscipit. Fusce commodo ac nisi non facilisis.
            Proin augue justo, porta ut sagittis at, feugiat id libero.
            Curabitur tempor mollis ex sed finibus. Suspendisse viverra
            condimentum elementum. Suspendisse potenti. Sed laoreet egestas sem
            quis faucibus. Fusce eget felis tempus, lacinia sem semper,
            fermentum lectus.

            Donec tincidunt, quam ut dictum facilisis, tortor leo imperdiet
            dolor, vel accumsan ante sem quis nisi. Pellentesque habitant morbi
            tristique senectus et netus et malesuada fames ac turpis egestas.
            Nam mollis mauris nec consequat finibus. Duis efficitur augue ut
            massa finibus commodo. Etiam imperdiet dui in ipsum iaculis
            placerat. Praesent eget mauris sapien. Ut non interdum quam. Morbi
            volutpat nisl ut ante sodales elementum. Vivamus lacinia tellus ac
            lacus posuere, id iaculis enim imperdiet. Curabitur faucibus, urna a
            interdum tincidunt, sem purus iaculis neque, quis rhoncus augue sem
            id sapien. Quisque cursus mollis euismod.

            Fusce efficitur augue quam, vel gravida mauris finibus a.
            Pellentesque habitant morbi tristique senectus et netus et malesuada
            fames ac turpis egestas. Fusce ligula nisi, posuere nec nisl et,
            auctor porttitor nulla. In hac habitasse platea dictumst. Fusce
            pharetra leo non hendrerit porttitor. Vestibulum sollicitudin id
            neque et tempor. Nam quis tellus lobortis, aliquam tellus semper,
            facilisis massa. Integer varius id nisl id suscipit.

            Praesent rutrum ligula ut vehicula ultrices. Morbi ullamcorper quis
            lorem ut bibendum. Fusce vehicula a eros eu consectetur. Curabitur
            tincidunt lacus sodales, vestibulum dui vel, efficitur mauris.
            Aliquam fermentum ligula a nunc fermentum consequat. Lorem ipsum
            dolor sit amet, consectetur adipiscing elit. Etiam nulla augue,
            dignissim et erat nec, auctor dapibus justo.

            Vivamus quis vestibulum lorem. Ut vel mauris ut metus porta
            efficitur sed sit amet purus. Cras sed felis ac sem elementum
            facilisis molestie et leo. Donec nec leo sit amet diam sollicitudin
            bibendum. Maecenas dui sem, semper a luctus auctor, consectetur at
            nisl. Nullam semper sapien lorem, quis auctor lectus mattis vel.
            Fusce gravida porttitor nunc eu rhoncus. Curabitur justo urna,
            gravida in lacus nec, tempus porta mauris. Vestibulum lacinia tortor
            magna, at feugiat leo suscipit et.";

    $headers = "From: dean@deanwebbdeveloper.com";

    if (mail($emailTo, $subject, $body, $headers)) {

        echo "The email was sent successfully";

    } else {

        echo "The email could not be sent.";

    }

 ?>
