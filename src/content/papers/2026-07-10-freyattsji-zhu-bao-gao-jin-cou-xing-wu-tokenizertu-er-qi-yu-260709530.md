---
title: FreyaTTS Technical Report
title_zh: FreyaTTS技术报告：紧凑型无Tokenizer土耳其语优先语音合成模型
authors:
- Ahmet Erdem Pamuk
- Ömer Yentür
- Ahmet Tunga Bayrak
- Yavuz Alp Sencer Öztürk
- Mustafa Yavuz
affiliations:
- Freya Team
arxiv_id: '2607.09530'
url: https://arxiv.org/abs/2607.09530
pdf_url: https://arxiv.org/pdf/2607.09530
published: '2026-07-10'
collected: '2026-07-13'
category: Other
direction: 语音合成 · 边缘端高效生成
tags:
- TTS
- Diffusion Transformer
- Non-Autoregressive
- Edge Deployment
- Speech Synthesis
one_liner: 183M参数无Tokenizer土耳其语TTS，基于非自回归DiT实现边缘设备高效高准确率语音合成
practical_value: '- 非自回归DiT+冻结预训练AudioVAE架构可复用在电商智能客服语音生成场景，大幅降低推理时延，适配移动端/边缘设备部署

  - 两阶段后训练方案（音色锁定+短语句覆盖）可直接迁移到客服语音定制场景，快速实现专属音色对齐，解决短指令/短query播报出错问题

  - 无Tokenizer端到端建模思路可复用在小语种跨境电商语音交互模块开发，省去复杂的音素转换前端开发成本'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有土耳其语TTS依赖复杂音素转换前端与离散Tokenizer，大参数模型难以适配边缘部署，对话场景下短语音鲁棒性、音色一致性表现较差。

### 方法关键点
1. 采用183.2M参数非自回归条件流匹配Diffusion Transformer（DiT）结构，在冻结的AudioVAE2连续隐空间训练，仅聚焦文本到隐空间映射，继承48kHz高音质重建能力
2. 端到端无额外Tokenizer/音素转换前端，直接基于92个土耳其字符词汇表训练，自动学习黏着语形态、元音和谐等语言特性
3. 非自回归并行去噪，同时预测整段隐序列避免自回归误差累积；配套两阶段生产级后训练：单说话人音色锁定+短语句覆盖，优化音色一致性和短输入鲁棒性

### 关键结果
在Freya-TR-Eval基准上WER 8.0%、CER 3.0%，效果优于参数量大得多的开源系统；消费级GPU实时因子0.11，笔记本CPU可超实时运行，适配边缘部署场景。
