---
title: StepAudio 3 Realtime Technical Report
title_zh: StepAudio 3 实时语音交互大模型技术报告
authors:
- Bin Lin
- Bo Zhao
- Boyang Zhang
- Boyong Wu
- Chao Yan
- Chen Geng
- Chen Wu
- Cheng Yi
- Chengli Feng
- Chenglin Zhu
affiliations:
- StepFun-Audio Team
arxiv_id: '2609.14005'
url: https://arxiv.org/abs/2609.14005
pdf_url: https://arxiv.org/pdf/2609.14005
published: '2026-09-11'
collected: '2026-09-16'
category: Agent
direction: 实时语音Agent · 全双工交互优化
tags:
- Voice-Agent
- Real-time-LLM
- Full-Duplex
- MoE
- Audio-Understanding
- Tool-Use
one_liner: 提出听-说-思-行闭环实时音频语言大模型，在全双工交互、语音Agent任务上达SOTA
practical_value: '- 全双工双音频流+320ms块级状态令牌的话语权管理架构，可直接迁移到电商语音导购/电话客服Agent，解决用户中途打断、插话、中途改需求的识别问题，提升交互自然度

  - Think-While-Speaking并行推理+输出的设计，可复用在直播实时话术生成、实时客服回复等低延迟要求的生成场景，平衡响应速度与推理深度

  - 小批量高质量SFT数据效果远超大批量低质量数据的结论，可复用在垂直场景Agent微调，将标注资源集中在高价值样本上，降本提效

  - 同基座多专精模型加权融合的方案，可用来整合电商不同场景（导购/售后/查单）的Agent能力，无需全量重训即可快速上线多能力模型'
score: 9
source: huggingface-daily
depth: full_pdf
---

### 动机
实时语音交互需要同时满足深推理、低延迟、自然轮次切换三个核心要求，现有音频大模型难以同时平衡推理深度和响应时延，也无法自然处理用户打断、多轮工具调用等复杂交互场景，限制了语音Agent的落地体验。

### 方法关键点
- 架构为MoE结构，总参数196B，单token激活参数11B，基于Qwen3-Omni音频编码器+Step 3.7 Flash语言基座，双音频流输入原生支持全双工交互
- 设计听-说-思-行闭环：Deep Perception模块做语音识别+音频理解，Seamless Duplex模块做会话话语权管理，Think-While-Speaking模块并行执行推理与语音输出，搭配Adaptive Thinking按需启动推理、MTP多令牌预测加速推理过程
- 语音Agent支持异步工具调用，工具执行过程中用户可正常对话，结果自动融入会话上下文
- 训练采用三阶段预训练+中训+SFT流程，SFT阶段优先保留高标注质量数据，最终通过多专精模型加权融合整合多场景能力

### 关键结果
- 全双工交互得分98.9，超过Qwen Audio 3.0 Realtime Plus的98.4、GPT-realtime-2的95.3，排名当前SOTA
- τ-Voice语音Agent任务宏观成功率56.0%，接近Grok的56.5%，优于Qwen的54.6%、GPT的45.7%
- 音频理解8个基准中4个排名第一，MMSU得分90.6，领先Gemini 3.1 Pro的83.6
- 100K高质量SFT数据效果远超2M随机采样数据，MMSU得分从78.78提升到89.70

### 值得记住的一句话
实时交互场景下，数据质量的优先级远高于数据规模，并行推理+输出的架构是平衡响应速度和推理深度的核心可行路径。
