---
title: Building and Evaluating Fixed-Voice Thai TTS from Synthetic Speech
title_zh: 基于合成语音的固定音色泰语TTS构建与评估
authors:
- Kunat Pipatanakul
- Potsawee Manakul
- Warit Sirichotedumrong
- Sittipong Sripaisarnmongkol
- Pakorn Nathong
- Phatrasek Jirabovonvisut
affiliations:
- Wayu Research
- Paxa Labs
- Typhoon
arxiv_id: '2609.03502'
url: https://arxiv.org/abs/2609.03502
pdf_url: https://arxiv.org/pdf/2609.03502
published: '2026-09-02'
collected: '2026-09-15'
category: Other
direction: 低资源语音合成 · 大模型知识蒸馏
tags:
- TTS
- Knowledge Distillation
- Low-Resource NLP
- On-device AI
- Speech Synthesis
one_liner: 仅用15秒参考音频生成训练数据，蒸馏得到82M参数量的端侧高性能固定音色泰语TTS
practical_value: '- 低资源场景无足量标注数据时，可采用大模型生成合成数据蒸馏小模型的方案，适配端侧低成本部署需求，可迁移至多语言电商语音播报、客服话术生成等场景

  - 多语言/混合语言生成任务中，需针对词边界歧义、专有名词、数词转写等领域痛点做前端预处理+质量过滤，可直接复用在跨境电商多语言内容生产链路

  - 蒸馏流程中需平衡数据过滤的精度与难例覆盖度，避免过度过滤导致模型泛化性下降，该经验适用于所有大模型蒸馏小模型的落地场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
低资源场景下TTS部署存在两难：大参数量语音克隆模型推理成本高，小型固定音色TTS需大量单说话人标注语料；泰语额外存在词边界歧义、声调、泰英代码切换、数词转写等挑战。
### 方法关键点
以大语音克隆模型为可编程数据源，仅输入15秒目标音色参考音频生成全量合成训练数据，通过优化文本预处理、质量过滤、拒绝采样、前端模块等流程，蒸馏得到小参数量学生TTS模型。
### 关键结果
82M参数量的端侧模型无需参考音频即可运行：挑战集关键词准确率68.2%（达Gemini 3.1的85.5%），停顿精度91.4%超过教师模型OmniVoice的89.9%，泰语CER 3.7%、英语CER 1.1%，停顿错误率为参比系统中最低。
