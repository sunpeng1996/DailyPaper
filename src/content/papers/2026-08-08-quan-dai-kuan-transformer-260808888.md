---
title: Full-bandwidth transformer
title_zh: 全带宽Transformer
authors:
- Xi Wang
- Ziyang Cai
- Zheng Zhan
- Harry Dong
- Ying Fan
- Gustavo de Rosa
- Tim Pearce
- John Langford
affiliations:
- Johns Hopkins University
- Princeton University
- Microsoft
arxiv_id: '2608.08888'
url: https://arxiv.org/abs/2608.08888
pdf_url: https://arxiv.org/pdf/2608.08888
published: '2026-08-08'
collected: '2026-08-14'
category: LLM
direction: LLM架构优化 · 隐状态反馈解码
tags:
- Transformer
- Latent Feedback
- KV Cache
- Pre-training Efficiency
- Decoding Optimization
one_liner: 通过隐状态反馈拓宽解码步间通道，仅增1%开销达到1.5倍训练数据的同等效果
practical_value: '- 生成式推荐/Agent推理场景可复用隐状态反馈思路：中间计算无需全部 verbalize 为token，将顶层隐状态回喂输入，可缩短生成长度降低延迟，不损失准确率，适配电商实时响应需求

  - 训练侧渐进式多轮反馈调度可直接复用：微调垂域小模型时无需全程开启反馈，中后期仅混3%三轮batch即可稳定获得性能增益，不损失并行训练效率

  - 方案完全兼容现有KV cache、vLLM推理栈，业务侧替换模型几乎无工程成本，可免费获得文案生成、query推荐等场景的效果提升

  - 垂域预训练场景可复用训练方案，同等训练数据下效果提升1.5-2倍，降低高成本电商/广告垂域数据的采集标注成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有自回归Transformer解码时步间反馈仅传递单个采样token，D维顶层隐状态直接丢弃，相当于将高维状态压缩到仅log2|V|比特的窄通道，非语言化的中间计算（推理中间结果、规划）无法回到底层重新计算，只能要么浪费token生成CoT，要么重复计算；同时高质量训练数据稀缺性日益凸显，亟需提升单token的计算利用率，在不显著增加推理成本的前提下提升模型效果。

### 方法关键点
- 隐状态反馈解码：每步解码时将上一步顶层隐状态与当前采样token embedding通过非对称GLU融合（隐状态走值路径，token做门，避免模型退化回普通结构）作为下一步输入，完全兼容KV cache、现有推理栈，单token解码开销增加<1%
- 并行多轮训练：通过多轮前向模拟序列依赖，保留teacher forcing并行性；采用渐进式调度：前期用普通单轮训练，中后期加入2轮batch，仅混3%的3轮batch即可让反馈映射形成收缩稳定点，支撑远长于训练时长的生成序列
- 稳定trick：隐状态缩放、融合后RMSNorm、embedding与输出层权重绑定、训练时加小噪声正则，保证长生成序列稳定性

### 关键结果数字
1B参数模型训练到400B tokens，验证损失、5-shot LM评测、数学/代码生成、指令微调效果全面优于同参数量同训练数据的普通Transformer，效果等价于1.5-2倍训练数据的普通Transformer，部分任务接近5倍数据基线；数学推理任务相同准确率下推理链长度缩短40%以上；即使不用隐状态解码，仅用该训练方案的普通Transformer也可获得显著效果提升。

最值得记住的一句话：通过复用解码时本会丢弃的顶层隐状态做反馈，仅用几乎可忽略的推理开销，就能换来等价于多50%训练数据的效果提升，同时完全兼容现有Transformer生态。
