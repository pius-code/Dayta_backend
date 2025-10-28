# Dayta Backend

A FastAPI-based backend service that allows Africans to buy mobile data from different vendors at competitive pricing. This backend enables you to integrate Dayta's services into your application.

## 🚀 Features

- **Buy Mobile Data**: Purchase data for MTN, AirtelTigo, and other supported networks
- **Check Balance**: Monitor your account balance
- **Provider Integration**: Currently supports Hubnet provider (more providers coming soon)
- **RESTful API**: Clean, documented endpoints with automatic OpenAPI/Swagger documentation
- **Async Support**: Built with async/await for high performance

## 📋 Prerequisites

- Python >= 3.13
- A provider account (recommended: [Hubnet](https://console.hubnet.app))
- API credentials from your provider

## 🛠️ Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd Dayta_backend
   ```

2. **Install dependencies using uv (recommended) or pip:**

   ```bash
   # Using uv
   uv sync

   # Or using pip
   pip install -e .
   ```

## ⚙️ Configuration

1. **Create a `.env` file** in the root directory:

   ```env
   PROV1_URL=https://console.hubnet.app/live/api/context/business/transaction
   API_KEY=your_api_key_here
   ```

2. **Environment Variables:**
   - `PROV1_URL`: Base URL for your provider's API
   - `API_KEY`: Your provider API authentication key

## 🚦 Running the Server

**Development mode with auto-reload:**

```bash
python main.py
```

The server will start on `http://localhost:8080`

**Access the API documentation:**

- Swagger UI: `http://localhost:8080/docs`
- ReDoc: `http://localhost:8080/redoc`

## 📡 API Endpoints

### Root

- **GET** `/` - Health check endpoint

### Buy Data

- **POST** `/buy/`
  - **Description**: Purchase mobile data for a given network
  - **Request Body**:
    ```json
    {
      "network": "MTN",
      "phone": "0241234567",
      "volume": "1000" 1GB in MB
    }
    ```
  - **Supported Networks**: MTN, AirtelTigo (AT), vodafone in the works

### Check Balance

- **GET** `/check_balance/`
  - **Description**: Get your current account balance
  - **Response**: Returns balance information from your provider account

## 📁 Project Structure

```
Dayta_backend/
├── main.py                 # Application entry point
├── pyproject.toml         # Project dependencies and metadata
├── .env                   # Environment variables (not in git)
├── core/
│   ├── config.py         # Configuration management
│   └── headers.py        # API headers setup
├── model/
│   └── payload.py        # Pydantic models for request/response
├── route/
│   ├── __init__.py       # Router aggregation
│   ├── buy_routes.py     # Data purchase endpoints
│   └── check_balance_route.py  # Balance check endpoints
└── utils/
    ├── outload_constructor.py   # Request payload builder
    └── safe_request.py          # HTTP client wrapper
```

## 🧪 Testing

You can test the API using:

- **Thunder Client** (VS Code extension)
- **Postman**
- **cURL**
- **httpie**

**Example using cURL:**

```bash
# Check balance
curl http://localhost:8080/check_balance/

# Buy data
curl -X POST http://localhost:8080/buy/ \
  -H "Content-Type: application/json" \
  -d '{
    "network": "MTN",
    "phone": "0241234567",
    "volume": "1000"
  }'
```

## 🔧 Dependencies

- **FastAPI**: Modern, fast web framework for building APIs
- **httpx**: Async HTTP client for making requests to providers
- **uvicorn**: ASGI server for running the application
- **python-dotenv**: Environment variable management
- **pydantic**: Data validation using Python type annotations

## 🤝 Contributing

This is an open-source project. Feel free to:

- Report bugs
- Suggest new features
- Submit pull requests
- Add support for more providers

## 📝 Notes

- Always use trailing slashes in endpoint URLs (e.g., `/buy/` not `/buy`)
- Network names may be case-sensitive depending on the provider
- Check your provider's documentation for supported network values and data volumes

## 🔜 Roadmap

- [ ] Add support for more providers
- [ ] Add support for Vodafone network
- [ ] Implement transaction history endpoint
- [ ] Add rate limiting
- [ ] Add authentication/API key management
- [ ] Add comprehensive error handling
- [ ] Add unit tests

## 📄 License

Open source - feel free to use and modify!

## 🐛 Troubleshooting

**Issue: "No parameters" in Swagger UI**

- Hard refresh the browser (Ctrl+Shift+R)
- Restart the FastAPI server.... its not working**_(cries in Python)_**

**Issue: 307 Redirect Error**

- Ensure you're using trailing slashes in URLs (`/buy/` not `/buy`)

**Issue: 400 Bad Request**

- Verify network name matches provider's accepted values
- Check the provider's dashboard for correct network identifiers
- Use browser DevTools to inspect frontend requests

---

**Made with PiLaDo for affordable data access in Africa**
