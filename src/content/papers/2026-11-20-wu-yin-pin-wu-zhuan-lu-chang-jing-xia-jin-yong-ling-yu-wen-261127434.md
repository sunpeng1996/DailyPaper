---
title: 'No Audio, No Transcripts, No Problem: LLM-based ASR Adaptation Using Only
  Domain Documents'
title_zh: 无音频无转录场景下仅用领域文档实现的LLM基ASR域适配
authors:
- Sergio Burdisso
- Dairazalia Sánchez-Cortés
- Esaú Villatoro-Tello
- Thibault Bañeras-Roux
- Manjunath K E
- Kadri Hacioglu
- Petr Motlicek
- Andreas Stolcke
affiliations:
- Idiap Research Institute
- Uniphore
- Brno University of Technology
arxiv_id: '2611.27434'
url: https://arxiv.org/abs/2611.27434
pdf_url: https://arxiv.org/pdf/2611.27434
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: LLM驱动语音识别零样本领域适配
tags:
- Domain Adaptation
- ASR
- Synthetic Data
- LLM
- Zero-shot Adaptation
one_liner: 仅用领域文档生成适配文本，实现效果接近真实转录的LLM基ASR域适配，同时开源基准数据集
practical_value: '- 电商语音客服ASR适配可复用该方案，无需采集标注客服语音，仅用现有客服知识库、产品文档即可快速完成新领域ASR冷启动，大幅降低标注成本

  - 书面知识转口语化合成的逻辑可迁移到语音类Agent的话术生成/语义理解模块，将结构化领域知识转成符合口语交互习惯的语料，提升对话准确率

  - 缺标注数据场景的域适配可参考「书面语直接用+LLM生成口语化语料」的双路数据增强方案，根据目标场景交互风格选择最优语料类型'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
LLM-based ASR面临域迁移性能下降问题，现有文本适配方案依赖真实口语转录文本，实际新客户落地场景通常仅能提供原始文档，无标注转录或音频数据。

### 方法关键点
1. 设计两种域适配语料生成路径：直接使用原始文档的书面句子，或调用LLM将文档生成合成口语对话
2. 两类语料均输入基于去噪的纯文本适配流程完成ASR微调

### 关键结果
跨域、域内、域外三类场景下，仅用文档的适配效果可匹配或接近使用真实转录的效果；书面/口语化生成方案的最优选择取决于目标场景的说话风格与生成语料规模；同时构建并开源了首个同时包含音频、转录、文档的基准数据集。
