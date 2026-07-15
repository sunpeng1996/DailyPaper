---
title: Encoder-Side Neuron Identification and Amplification for Acoustic Perception
  in Large Audio-Language Models
title_zh: 面向大型音频语言模型声学感知的编码器侧神经元识别与放大
authors:
- Yu-Han Huang
- Chih-Kai Yang
- Ke-Han Lu
- An-Yu Cheng
- Hung-yi Lee
affiliations:
- National Taiwan University, Taiwan
- Graduate Institute of Communication Engineering, National Taiwan University, Taiwan
- NTU Artificial Intelligence Center of Research Excellence (NTU AI-CoRE), Taiwan
- ASUS Open Cloud Infrastructure Software Center, Taipei, Taiwan
arxiv_id: '2607.11801'
url: https://arxiv.org/abs/2607.11801
pdf_url: https://arxiv.org/pdf/2607.11801
published: '2026-07-13'
collected: '2026-07-15'
category: Multimodal
direction: 多模态大模型 · 推理侧性能优化
tags:
- LALM
- Acoustic Perception
- Inference Optimization
- Neuron Activation
- Multimodal LLM
one_liner: 提出无训练无标注的IAAN方法，推理时放大编码器高得分神经元，大幅提升LALM非语义语音属性识别精度
practical_value: '- 多模态语音交互类Agent（如电商导购、智能客服）可复用该神经元激活对比思路，无需重训即可提升情绪、语气等非语义语音特征识别精度，优化交互体验

  - 该推理侧优化思路可迁移至多模态推荐的图文/音视频编码器，通过对比真实输入与噪声参考的激活差异定位关键神经元，放大后提升细粒度特征识别效果，规避全量重训成本

  - 验证了编码器侧细粒度干预效果远优于decoder/LLM侧干预，做多模态召回/排序的编码器优化时可优先考虑编码器内部神经元级调优，而非后续链路干预'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
大型音频语言模型（LALM）在语音内容识别上表现优异，但对情绪、语气等非语义细粒度声学属性识别效果差；现有推理侧优化多在编码器后做粗粒度干预，未探索编码器内部神经元级优化空间，且需避免重训成本。
### 方法关键点
提出无训练无标注的IAAN方法：1）构造不含真实声学信息的噪声参考输入，对比音频编码器每个前馈神经元对真实波形、噪声输入的激活差异，输出每个神经元的声学得分；2）推理时仅放大得分最高的小部分神经元激活值，无需修改模型结构或重训。
### 关键结果
在10项非语义语音属性任务上，IAAN为Audio-Flamingo-3提升平均准确率25.7pp，为Qwen2.5-Omni提升21.4pp，为Kimi-Audio提升9.7pp，对已针对声学证据微调的模型仍有增益；对照组验证仅编码器侧神经元级精准干预有效，编码器后、解码侧或LLM内部干预基本无收益甚至降准。
