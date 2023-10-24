//write javascript code that reads a file and prints lines containing text input from user?

// Get file input from user
const fileInput = document.createElement('input');
fileInput.type = 'file';
fileInput.onchange = (e) => {
 const file = e.target.files[0];
 const reader = new FileReader();

 reader.onload = (e) => {
    const fileContent = e.target.result;
    const lines = fileContent.split('\n');

    // Get text input from user
    const textInput = prompt('Enter the text you want to search for:');

    // Print lines containing the text input
    lines.forEach((line) => {
      if (line.includes(textInput)) {
        console.log(line);
      }
    });
 };

 reader.readAsText(file);
};

document.body.appendChild(fileInput);
fileInput.click();