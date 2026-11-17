---
title: 'AITHER: Authority-Informed Evidence Routing for Mixed-Authority Vision-Language
  Reasoning'
title_zh: AITHER：面向混合权限多模态推理的权限感知证据路由机制
authors:
- Xinjin Li
- Haoyue Zhang
- Xinyi Gou
- Yuruo Gong
- Yuanjian He
- Muzi Li
- Yujian Long
- Yu Ma
- Yiliu Xu
- Tianxin Zhou
affiliations:
- Columbia University
- UC Berkeley
- Texas A&M University
- Rice University
- Sun Yat-sen University
arxiv_id: '2611.18735'
url: https://arxiv.org/abs/2611.18735
pdf_url: https://arxiv.org/pdf/2611.18735
published: '2026-11-10'
collected: '2026-11-17'
category: Multimodal
direction: 多模态推理 · 证据路由
tags:
- Multimodal Reasoning
- Evidence Routing
- Black-box Control
- Vision-Language Model
- Hallucination Mitigation
one_liner: 提出训练免的语义帧路由层AITHER，解决混合权限场景下多模态推理的输入优先级仲裁问题
practical_value: '- 电商多模态导购Agent可复用训练免的语义帧路由架构，对用户指令、商品图、商品描述三类输入做权限分级仲裁，避免合法指令被多模态信息错误覆盖

  - 多模态广告素材合规校验场景可借鉴权限分层逻辑，优先遵循平台规则指令，再校验素材与描述的一致性，大幅降低规则类误判率

  - 多模态商品搜索模块可引入语义极性解析步骤，对用户query、商品图文的冲突信息做显式优先级排序，减少不符合用户预期的召回结果'
score: 7
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有多模态推理方法未显式定义不同输入的权限优先级，遇到图文冲突时默认优先采信图像信息，既会错误覆盖合法的任务指令/上下文规则，也无法针对性校正虚假声明类文本，输出结果稳定性差。
### 方法关键点
提出AITHER框架，核心是训练免的黑盒Semantic-Frame Router控制层，按固定流程执行路由：1）显式解析并锁定最高优先级的任务指令；2）从无元数据图像中恢复标准化空间帧；3）解析剩余文本的语义极性；4）在可观测候选结果间做带失败关闭语义的路由，将权限仲裁从不可控的prompt偏好转化为可复现的标准化推理流程。
### 关键结果数字
在1620条MATRIX预测集上准确率达95.1%，超出最强基线9.1个百分点，无任何负向效果样本；在1800条受控FRAME预测集上准确率达100%，GQA-MATRIX数据集上准确率达93.3%，同时实现虚假声明校正、任务规则保留、过校正消除三个核心目标。
