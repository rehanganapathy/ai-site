# ai-site
A website that uses python in the backend running on aws lambda and apiGateway that calls OpenAi(daVinci) to create taglines based on keywords you enter, a Full Stack web App

You can view it here:
https://ai-site-theta.vercel.app/

but at the moment it wont give you any results cause i have disabled my OpenAi key, but just copy the code and use your key in a .env file and you're all set

run ./generate_base_layer to create a zip folder to upload to aws using cdk deploy, so that all the dependencies are available for the lambda function to use
<img width="1342" alt="Screenshot 2022-08-04 at 00 20 05" src="https://user-images.githubusercontent.com/79349712/182688207-96fea6d1-0b57-4933-9389-910dceeb8722.png">
