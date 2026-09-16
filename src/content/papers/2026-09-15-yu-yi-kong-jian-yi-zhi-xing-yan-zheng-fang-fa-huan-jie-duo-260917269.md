---
title: Semantic-Spatial Agreement Verification for Mitigating Object Hallucination
  in Multimodal Large Language Models
title_zh: 语义-空间一致性验证方法缓解多模态大模型物体幻觉问题
authors:
- Ziheng Ren
- Qian Gao
- Jun Fan
- Guohui Ding
- Zhenyu Yang
- Yuteng Xiao
affiliations:
- Qilu University of Technology (Shandong Academy of Sciences)
- Key Laboratory of Computing Power Network and Information Security, Ministry of
  Education
arxiv_id: '2609.17269'
url: https://arxiv.org/abs/2609.17269
pdf_url: https://arxiv.org/pdf/2609.17269
published: '2026-09-15'
collected: '2026-09-16'
category: Multimodal
direction: 多模态大模型 · 幻觉抑制
tags:
- Multimodal LLM
- Hallucination Mitigation
- Training-free
- Semantic Consistency
- Spatial Consistency
one_liner: 提出免训练的语义-空间一致性验证框架，缓解多模态大模型物体幻觉问题
practical_value: '- 电商多模态商品理解、图生文案场景可复用该免训练校验思路，通过同义query结果语义一致性+物体空间重叠度校验，降低内容幻觉率

  - 多模态导购Agent、线下巡检Agent的视觉感知模块可集成SSAV逻辑，无需微调基座即可提升视觉信息提取准确率，降低落地成本

  - QIRV的跨query区域重叠度、候选优势度计算逻辑可直接复用到多模态召回结果置信度打分模块，无需额外标注数据'
score: 7
source: arxiv-cs.CV
depth: abstract
---

### 动机
多模态大模型（MLLM）基于视觉输入生成文本时易提及图像中不存在的物体，在医疗辅助、环境决策等场景存在实质安全风险，现有幻觉优化方案多需微调基座，落地成本高。
### 方法关键点
1. 提出免训练的SSAV框架，聚合多个同义prompt估计语义支持度，降低query措辞对校验结果的干扰；
2. 设计QIRV模块，结合跨query区域持久性、空间重叠度、候选相对优势度三类指标，识别孤立高响应、分散定位等异常情况；
3. 用几何均值融合语义、空间两路证据，任意一路支持度不足时自动降低校验得分。
### 关键结果
在LLaVA-1.5-7B上测试，COCO、A-OKVQA、GQA平均准确率在POPE Popular、Adversarial设置下分别提升1.81、3.17个百分点，CHAIRs幻觉指标从49.40%降至32.80%。
