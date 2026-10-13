---
title: 'When VLMs Destroy What They Know: Spatial Representations Fall Below Lexical
  Priors'
title_zh: 多模态大模型内部缺陷：空间表征可信度远低于词汇先验
authors:
- Shubh Garg
- Chen Shani
affiliations:
- Thapar Institute of Engineering and Technology
- Tel Aviv University
arxiv_id: '2610.13910'
url: https://arxiv.org/abs/2610.13910
pdf_url: https://arxiv.org/pdf/2610.13910
published: '2026-10-09'
collected: '2026-10-13'
category: Multimodal
direction: 多模态大模型 · 内部表征评估
tags:
- VLM
- Representation Evaluation
- Spatial Reasoning
- Benchmark
- Causal Intervention
one_liner: 提出EICS度量与CASP-VL基准，揭示VLM全局表征会丢失可被单token识别的空间关系信息
practical_value: '- 做多模态商品检索/图文匹配场景时，避免直接用VLM全局EOS/mean pooling表征做空间相关匹配，可补充谓词token局部特征缓解位置相关bad
  case

  - 若下游任务涉及空间关系判断（如电商商品摆放合规检测、家居搭配位置合理性校验），微调VLM时可增加谓词token表征对齐损失，减少空间信息丢失

  - 可复用EICS度量评估自微调VLM在特定业务概念上的表征稳定性，避免仅看输出准确率忽略模型依赖统计先验蒙对答案的伪成功问题'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有VLM仅靠输出端评估无法判断内部表征是否真实编码了推理所需的结构化关系，无法解释模型靠统计先验蒙对答案的伪成功问题。
### 方法关键点
1. 提出EICS（评估不变概念稳定性）度量，定量测试单概念受控干预下模型表征的编码一致性
2. 构建CASP-VL基准，基于Visual Genome场景图生成因果受控的空间扰动样本，针对性评估空间关系表征保真度
### 关键结果
- 跨多架构VLM测试显示，空间关系表征的保真度显著低于词汇信息，即使模型在组合推理基准上得分远高于随机水平
- 空间关系信息在谓词对应token层面可被识别，但经过EOS token或均值池化生成全局表征后完全丢失
- 这类缺陷完全无法被输出端评估发现，属于VLM内部表征的系统性故障
