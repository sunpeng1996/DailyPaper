---
title: Incongruence-Aware Evaluation of Multimodal Speech Emotion Recognition in Audio
  Large Language Models
title_zh: 音频大语言模型多模态语音情感识别的不一致感知评估
authors:
- Fengji Jing
- Guy Laban
affiliations:
- The University of Hong Kong
- Ben-Gurion University of the Negev
arxiv_id: '2610.40883'
url: https://arxiv.org/abs/2610.40883
pdf_url: https://arxiv.org/pdf/2610.40883
published: '2026-10-29'
collected: '2026-11-02'
category: Eval
direction: 多模态大模型 · 鲁棒性评估
tags:
- Multimodal LLM
- Speech Emotion Recognition
- Cross-Modal Incongruence
- Model Evaluation
- Valence-Arousal-Dominance
one_liner: 提出无阈值跨模态不一致度评分，验证音文冲突会大幅升高音频大模型语音情感识别错误率
practical_value: '- 语音交互类Agent（电商智能客服、语音导购等）落地时，可复用本文跨模态不一致度评分，提前识别音文冲突的高风险输入，降级走兜底逻辑

  - 多模态LLM优化优先级可向模态融合策略倾斜，本文验证了融合逻辑而非单模态特征是多模态任务错误的核心来源

  - 多模态模型评估环节，可引入无标注的不一致度指标作为鲁棒性测试项，无需人工标注即可预判模型泛化风险'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
语音交互LLM需同时处理文本语义与声学特征，两类模态信息常存在冲突，现有评估体系未量化这种不一致对性能的影响，也缺乏无需标注的通用评估指标。
### 方法关键点
将文本、音频映射到效价-唤醒度-支配度（VAD）共享空间，采用双分量高斯混合模型将模态间距离转换为连续无阈值的不一致度评分，无需依赖情感词典或人工标注即可计算。
### 关键结果
在3类语音数据集（表演型eNTERFACE'05、对话型MELD、自然型CMU-MOSEI）上测试3个音频大模型，控制真值情绪、特征空间距离等变量后，只要音频输入存在，模态不一致就会使识别错误概率在所有数据集上显著升高；仅替换文本编码器就可使单文本效果在某数据集上符号反转，纯文本效果可靠性差；该评分是6个备选方案中唯一能在所有3个数据集上预测模型错误的无标注指标。
