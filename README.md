# Mathematics-divulgative-tools

 I have been working on a mathematical divulgative project, particularly on number theory and its applications, covering many different topics. In the initial process, I encountered many difficulties in uploading content, as Instagram is a social network that compresses photos and I had no idea where or how to create the material.

## The solution:

We started using Beamer in LaTeX. Beamer is clearly not made for uploading content to Instagram, but over time, we have been able to adapt a lot of tools so that the quality of the content we handle is the best possible. We changed the aspect ratio of the presentations to a square style and found some good templates to work with. At this point, the problem was "how to convert the PDF project into good quality images for Instagram?" We used many software programs at the beginning, but the quality of none of them convinced us, so we decided to program our own tools. We will leave all the material we use for this purpose here, including the programs that help us process the PDF and convert them into images, as well as the Beamer template we use, etc.

<center><img src="https://github.com/mmanosalva/Mathematics-divulgative-tools/blob/main/Images/Style.png" width="80%"></center> 

  ## How to use PDF to PNG converter:

   To use this script, you will need to install Wand on your computer. Additionally, you will need to install ImageMagick and add it to the Windows path. Finally, you will need to install Ghostscript.

   To install Wand you will need python first. Open CMD or your Linux Terminal: 

   ```shell
   pip install Wand
   ```
  
  That will install Wand

  Now go to [Install ImageMagick](https://imagemagick.org/script/download.php#windows) and - [Ghostscript](https://ghostscript.com/releases/gsdnld.html), install and remember to add them both to path.

  Perhaps the process is automatic in your case, but it is better to make sure.

  For linux users its easier to install Imagemagick and Ghostscript from terminal, so DO IT.

  I won't explain how the program's interface works because we made it as user-friendly as possible. Just make sure that the PDF is in the same folder as the .py file.



