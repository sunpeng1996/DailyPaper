---
title: 'OpenGlass: A Sensing-Computing Split Architecture for Local MLLM-Driven Real-Time
  Visual Assistance'
title_zh: OpenGlass：面向本地MLLM实时视觉辅助的感知计算拆分架构
authors:
- Mengzhang Li
- Yuan Yao
affiliations:
- Shanghai Qizhi Institute
- Tsinghua University
arxiv_id: '2607.03213'
url: https://arxiv.org/abs/2607.03213
pdf_url: https://arxiv.org/pdf/2607.03213
published: '2026-07-03'
collected: '2026-07-07'
category: Multimodal
direction: 多模态大模型 · 端侧实时部署
tags:
- MLLM
- Edge Deployment
- Low Latency
- Privacy First
- Visual Assistant
one_liner: 面向视障群体的开源感知-计算拆分架构，本地运行MLLM实现低延迟高隐私的实时视觉辅助
practical_value: '- 可复用感知-计算拆分架构：低算力穿戴/IoT端仅做数据采集，高算力就近设备（手机/随身主机）跑MLLM推理，平衡功耗、延迟、隐私，适合AR导购、线下店视觉Agent等场景

  - 直接复用延迟优化trick：输入图像提前resize减少VLM切片数、流式输出分句喂TTS、关闭模型think模式，可将实时多模态交互类Agent（如直播数字人、导购助手）响应延迟降低30%以上

  - 安全机制可迁移：分任务设计强制abstention规则+全链路可审计日志，避免多模态模型幻觉输出错误引导，适合电商导购、广告投放等对准确性要求高的场景'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
云侧MLLM视觉助手需上传第一人称视觉数据，隐私风险高，且网络延迟普遍达数秒，无法满足视障用户实时导航、物品识别等场景的低延迟需求；而穿戴设备算力功耗有限，无法直接运行大模型，存在体验与隐私的核心矛盾。

### 方法关键点
- 感知-计算拆分架构：ESP32低成本眼镜端仅负责图像采集，就近消费级设备（笔记本/后续支持手机）本地运行INT4量化MLLM推理+ASR/TTS，原始视觉数据默认不流出用户可控设备
- 延迟优化设计：图像提前resize减少VLM输入切片数，模型输出流式分句直接喂TTS，无需等待完整响应再播报
- 安全防护设计：分任务设定强制abstention规则，识别不清时主动要求用户重拍，禁止幻觉编造内容，配套全链路可审计日志方便定位错误

### 关键结果
基于120条真实ESP32采集的视障场景数据集，对比云侧Gemini 2.5 Flash、Qwen-VL-Max和未优化端侧基线：resize后端到端用户到音频延迟中位数993ms，97.5%请求低于2s，比国内云基线Qwen-VL-Max快1倍以上，比海外云基线Gemini快4倍；图像resize是最大延迟优化点，resize到448px可降低TTFT 66%，仅伴随轻微质量下降。

最值得记住的一句话：本地优先的多模态系统不仅能解决隐私问题，在延迟稳定性上也远超云侧方案，是实时交互类多模态Agent的核心落地路径。
