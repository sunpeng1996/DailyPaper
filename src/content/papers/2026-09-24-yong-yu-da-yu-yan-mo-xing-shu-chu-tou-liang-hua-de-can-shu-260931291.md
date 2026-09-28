---
title: Softmax Reparameterization for Output-Head Quantization
title_zh: 用于大语言模型输出头量化的Softmax重参数化方法
authors:
- Asim Kadav
- Christian Flores
- Chirag Arora
- Varun Kotte
- Hongbo Zheng
- Lan Yan
- Priya Shanmugasundaram
- Tracy Holloway King
affiliations:
- Adobe SDC
arxiv_id: '2609.31291'
url: https://arxiv.org/abs/2609.31291
pdf_url: https://arxiv.org/pdf/2609.31291
published: '2026-09-24'
collected: '2026-09-28'
category: LLM
direction: LLM输出头低比特量化 推理效率优化
tags:
- Quantization
- SLM
- Softmax
- Inference Optimization
- Low-bit
one_liner: 提出训练后Softmax重参数化方法，大幅降低SLM输出头低比特量化的精度与延迟损失
practical_value: '- 部署端侧/边缘SLM做生成式推荐、Agent意图识别时，可复用该重参数化方法对输出头做W4量化，在几乎无损精度的前提下降低推理延迟约10%，适配低算力设备

  - 大vocab场景（如电商多语言商品标题生成、多语种Query推荐）的输出层量化无需重训，仅通过14个候选值的一维网格搜索即可选最优偏移系数，落地成本极低

  - 量化时可放弃固定均值中心化的默认策略，改用验证集KL最小化选择偏移量，在RTN、AW-MSE、GPTQ等主流量化方案下均能进一步降损，且与通道缩放、仿射量化等优化完全兼容'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前小语言模型（SLM）普遍采用大词表设计，输出头占总参数量的10%~17%，且每步解码需做全词表投影，是推理内存与延迟的核心瓶颈。现有训练后量化方案直接量化输出头会严重损失下一词预测精度，因此业界常保留输出头为BF16精度，浪费了大量优化空间。

### 方法关键点
- 利用Softmax仅依赖相对logit的特性，在输出头所有权重行减去偏移系数t乘以词表行均值，全精度下完全不改变Softmax输出分布
- 无需重训或修改解码器，仅通过14个候选值的一维网格搜索，以验证集上量化后输出与原模型的KL散度最小为目标选最优t，覆盖原头（t=0）和固定均值中心化（t=1）两个基线
- 对带tanh软截断等非线性logit路径的模型，通过秩一修正恢复偏移量保证等价性，兼容所有主流量化方案

### 关键结果
在WikiText、C4、OpenWebMath等数据集测试7个主流SLM：W4量化下Phi-4-mini的AW-MSE量化KL从0.936降至0.256，XGLM的RTN量化KL下降93%，效果优于固定均值中心化；偏移系数跨域迁移性强，WikiText选出的系数在C4、OpenWebMath上均优于固定均值中心化；部署端Phi-4-mini采用W4量化输出头，batch 1推理延迟较BF16基线降低10.8%，精度损失几乎可忽略。

**最值得记住的结论**：输出头的精度要求不取决于它表示的函数，而取决于它的参数化方式，合理利用Softmax的等价变换可在完全不损失功能的前提下大幅降低量化损失。
