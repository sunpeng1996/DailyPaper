---
title: Latent space bias directions in LLMs capture confidence, not fairness
title_zh: 大语言模型隐空间偏差方向实际编码置信度而非公平性
authors:
- Stephanie Buttigieg
- Maeve Madigan
- Parameswaran Kamalaruban
- Stuart Burrell
affiliations:
- University of Cambridge, UK
- Visa Inc. UK
arxiv_id: '2610.08559'
url: https://arxiv.org/abs/2610.08559
pdf_url: https://arxiv.org/pdf/2610.08559
published: '2026-10-06'
collected: '2026-10-07'
category: LLM
direction: LLM 可解释性 · 激活控制去偏
tags:
- activation steering
- LLM fairness
- latent space
- interpretability
- debiasing
one_liner: 揭示LLM激活steering去偏方向实际编码置信度，现有去偏效果来自置信度降低而非偏差修正
practical_value: '- 电商/广告场景做LLM驱动的文案生成、智能客服Agent去偏时，不要盲目使用activation steering类方法，这类方法会大幅提升模型拒答/输出不确定内容的概率，反而降低业务转化

  - 做LLM行为控制（如调整推荐偏好、控制输出风格）时，要验证steering vector是否与置信度方向混淆，避免出现控制了目标属性但连带降低输出确定性的副作用

  - 评估LLM去偏效果时，不能仅看偏差指标，需额外加测输出熵、拒答率、通用任务准确率，避免误判为去偏有效实际是置信度下降的假象'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
激活steering是当前主流的LLM推理侧轻量去偏方案，但此前研究发现其泛化性差、易损伤通用任务性能，且去偏效果不稳定。为明确隐空间中学习到的去偏方向真实编码的语义，避免去偏方案的不可靠风险，展开本次研究。

### 方法关键点
- 测试覆盖Llama-3.1-8B、Falcon3-7B、Ministral-3-8B、Qwen3.5-9B 4个系列共8个模型，含预训练、指令微调两个版本
- 基于BBQ、CrowS-Pairs、StereoSet三类偏差数据集，通过对比正反偏差样本隐状态训练线性分类器，提取去偏steering vector
- 同时在无偏差的MMLU、OpenBookQA通用知识数据集上提取置信度方向，对比两类方向的空间对齐度及steering干预后的行为变化

### 关键结果
- 偏差分类器区分高/低置信度样本的AUROC最高达0.94，而区分真实偏倚样本的AUROC仅0.57，说明分类器实际学习到的是置信度特征
- 去偏方向与通用置信度方向的余弦相似度最高达0.91，二者高度耦合
- 沿去偏方向steering后，Llama-3.1-8B-Instruct在BBQ模糊场景偏差得分从0.08降至0.01，但拒答率从24%升至99%，通用知识任务准确率最高下降6pct，输出熵平均提升30%以上

### 核心结论
基于激活steering的去偏效果本质是通过降低模型整体置信度实现的，并没有修正模型底层的偏差偏好，相关结果解读需要极其谨慎。
