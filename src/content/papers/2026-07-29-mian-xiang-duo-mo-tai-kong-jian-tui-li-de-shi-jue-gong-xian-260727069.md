---
title: Visual Credit Audit for Multimodal Spatial Reasoning
title_zh: 面向多模态空间推理的视觉贡献审计方法
authors:
- Feixiang Liu
- Qiang Qiu
- Lanbo Sun
- Nan Wei
- Huawei Shen
- Xueqi Cheng
affiliations:
- 中国科学院计算技术研究所AI安全国家重点实验室
- 中国科学院大学
arxiv_id: '2607.27069'
url: https://arxiv.org/abs/2607.27069
pdf_url: https://arxiv.org/pdf/2607.27069
published: '2026-07-29'
collected: '2026-07-31'
category: Eval
direction: 多模态大模型 · 空间推理能力评估
tags:
- MLLM
- Multimodal Evaluation
- Spatial Reasoning
- Visual Credit Audit
- Hallucination Detection
one_liner: 提出无训练无标签的多模态空间推理视觉贡献审计框架VCA，拆分答案正确性与视觉信息依赖度
practical_value: '- 电商多模态商品理解场景可复用VCA框架，审计大模型的商品属性、位置关系判断是否真的依赖商品图像而非文本先验，减少虚假推理导致的商品打标错误

  - 多模态搜索/推荐的MLLM模块上线前，可参考D-CC指标量化模型对视觉信息的实际利用率，筛选低幻觉的模型版本

  - 多模态Agent做AR导购、实景商品识别等空间交互任务时，可用VCA的控制变量法验证模型是否正确响应视觉关系变化，降低决策错误率'
score: 6
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有多模态空间推理的封闭yes/no基准存在缺陷，即使模型未用到图像信息、仅靠文本先验猜对答案也会被判定为正确，无法区分答案是基于真实视觉推理还是依赖先验蒙对。
### 方法关键点
VCA审计框架设置纯文本、空白对照组，拆分两个评估维度：一是模型决策是否从基准图像获得了比对照组更多的支持，二是模型是否响应关系特定的视觉证据；第一部分审计无需训练、无需标签，也不需要模型答案翻转，结合标签可生成依赖可信正确率（D-CC）指标，同时可扩展到错误样本的审计。
### 关键结果
在4个开源MLLM、2个空间推理基准上测试，12.73%~26.25%的正确答案实际未用到图像信息；同拆分图像置换后D-CC下降21.25~47.80个百分点；在受控的「正确但无视觉贡献」样本中，81.57%~100%的模型会对视觉关系反转做出响应，32.11%的样本会改变答案。
