---
title: 'Apriel Voice 27B Preview: An Open Model for Speech, Reasoning, and Tool Use'
title_zh: Apriel Voice 27B 预览：支持语音、推理与工具调用的开源模型
authors:
- Aman Tiwari
- Akshay Kalkunte
- Akintunde Oladipo
- Jash Shah
- Tara Bogavelli
- Hoang Nguyen
- Nishanth Madhusudhan
- Vishal Juneja
- Sridhar Nemala
- Srinivas Sunkara
affiliations:
- ServiceNow
arxiv_id: '2610.40738'
url: https://arxiv.org/abs/2610.40738
pdf_url: https://arxiv.org/pdf/2610.40738
published: '2026-10-28'
collected: '2026-11-02'
category: Agent
direction: 语音Agent · 多模态统一推理与工具调用
tags:
- Speech-Agent
- Multimodal-LLM
- Tool-Calling
- MoE
- Knowledge-Distillation
one_liner: 基于Gemma 4 26B的开源语音语言模型，统一多模态推理、对话与工具调用能力
practical_value: '- 语音Agent训练可复用两阶段适配方案：第一阶段冻住骨干训语音投影器，第二阶段联合微调投影器+骨干+CE/FKL混合损失，兼顾新模态适配与原有能力留存，适合现有文本Agent快速扩展语音交互能力

  - 多模态训练数据构造可复用trick：合成对话时自动选择语音/文本混合跨度，同一会话内统一参考语音，保留结构化信息（如订单ID、SKU编码）为文本，避免语音识别错误影响关键信息提取，可直接迁移到电商语音客服/导购Agent的数据生产流程

  - 大模型在线蒸馏工程优化方案：本地教师服务+批前瞻调度重叠教师推理与学生训练计算，融合全词表损失减少显存占用，3天即可完成27B级MoE模型的语音适配，适合业务侧快速迭代多模态Agent

  - 语音Agent效果评估可参考EVA/τ-Voice等行业benchmark，同时关注准确率-延迟-交互体验的trade-off，电商语音导购可针对性调整thinking模式开关平衡推理效果与响应速度'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
传统语音助手多采用ASR-LLM-TTS三级级联架构，模块割裂导致上下文理解、推理与工具调用能力脱节，无法满足复杂任务（如企业工单、电商客服）的多轮交互需求；现有开源语音模型多侧重识别翻译能力，缺乏端到端的推理与工具调用支持。
### 方法关键点
- 架构：基于Gemma 4 26B-A4B MoE骨干，新增Whisper large-v3-turbo语音编码器+47M参数投影器，保留原生文本、图像输入接口，统一支撑多模态理解、对话推理、工具调用，TTS模块可独立替换无需重训骨干
- 训练：两阶段适配：Stage1冻住骨干训投影器，覆盖多语种转录、翻译、续写任务；Stage2联合微调投影器+骨干，采用CE/FKL混合源依赖损失，配合文本回放保留原有能力，在线蒸馏用本地教师服务+计算重叠优化效率
- 数据：自动构造语音条件对话，自动选择用户输入中的语音/文本混合跨度，同会话统一参考语音，保留结构化标识符为文本，经保真度校验后用于训练
### 关键结果
- 语音推理：思考模式下Big Bench Audio得分98.90、Speech-BFCL得分81.13，为开源2阶段语音模型最优水平
- 任务表现：EVA准确率51.27%、体验pass@1 74.13%，τ-Voice任务成功率65.51%、平均延迟1.91s，接近闭源GPT-realtime-2.1表现
- 能力留存：文本、图像能力相比原生Gemma 4 26B下降不足1%，数学推理、工具调用能力基本持平

> 语音Agent的核心竞争力不是识别准确率，而是端到端的推理、工具调用与自然交互体验的综合平衡
