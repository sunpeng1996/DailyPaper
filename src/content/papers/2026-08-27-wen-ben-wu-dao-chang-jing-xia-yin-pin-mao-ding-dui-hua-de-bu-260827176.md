---
title: 'When Text Misleads: Inconsistent-Aware Reasoning for Audio-Grounded Dialogue'
title_zh: 文本误导场景下音频锚定对话的不一致感知推理方法
authors:
- Yen-Ju Lu
- Yuzhe Wang
- Yaohan Guan
- Xiluo He
- Jiarui Hai
- Mingrui Liang
- Kaavya Chaparala
- Thomas Thebaud
- Laureano Moro-Velazquez
- Najim Dehak
affiliations:
- Center for Language and Speech Processing, Johns Hopkins University
arxiv_id: '2608.27176'
url: https://arxiv.org/abs/2608.27176
pdf_url: https://arxiv.org/pdf/2608.27176
published: '2026-08-27'
collected: '2026-08-28'
category: Multimodal
direction: 多模态对话 · 跨模态冲突推理
tags:
- Multimodal Reasoning
- Speech Understanding
- Cross-modal Alignment
- Benchmark
- Agentic Framework
one_liner: 提出跨模态冲突基准ContraTalk与Audio Twin推理框架，解决语音对话理解的纯文本捷径问题
practical_value: '- 电商语音客服/导购场景可复用Audio Twin思路，将用户语气、韵律等声学特征转成文本可读表示输入LLM，避免纯转录文本的意图识别偏差

  - 多模态用户意图理解/内容审核场景可借鉴跨模态冲突检测框架，提前识别转录文本与音频情绪/真实意图不一致的风险case

  - 多模态Agent效果评估可参考ContraTalk构造逻辑，补充冲突样本集避免模型学习捷径，提升落地鲁棒性'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
语音对话理解需联合文本转录和声学特征（情绪、韵律等）推理，但现有模型常依赖纯文本捷径，当转录与声学信号冲突时会输出错误结果，且缺乏针对性评估基准。
### 方法关键点
1. 定义跨模态不一致故障模式，构建ContraTalk可控基准，包含501个QA样本，覆盖交互行为、情绪状态、对话动作等5个维度，同步包含跨模态一致/冲突两类样本；
2. 提出类Agent推理框架，将音频转换为文本可读的局部声学特征表示Audio Twin，为推理模型提供明确的声学证据输入。
### 关键结果
纯文本LLM在一致样本准确率超90%，冲突样本仅33-48%；原生AudioLLM仍有30-40%概率落入文本偏差陷阱；Audio Twin框架可提升冲突样本准确率，同时降低陷阱选择率，一致样本表现依赖基座模型能力。
