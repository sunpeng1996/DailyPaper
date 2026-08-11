---
title: 'From Diagnosis to Correction: Benchmarking and Improving Real-World Table
  Parsing'
title_zh: 从诊断到修正：真实场景表格解析的基准构建与性能优化
authors:
- Jutao Xiao
- Yuan Qu
- Dongsheng Ma
- Fan Wu
- Tianyao He
- Weihong Li
- Jie Yang
- Yu Qiao
- Bin Wang
- Conghui He
affiliations:
- 浙江大学
- 上海人工智能实验室
- 北京大学
arxiv_id: '2608.09842'
url: https://arxiv.org/abs/2608.09842
pdf_url: https://arxiv.org/pdf/2608.09842
published: '2026-08-10'
collected: '2026-08-11'
category: Agent
direction: Agent 框架优化冻结表格解析器性能
tags:
- Agent
- Table Parsing
- Visual Consistency
- Frozen Model
- Benchmark
one_liner: 构建细粒度表格解析诊断基准，提出无需重训的DEC Agent框架提升冻结解析器效果
practical_value: '- 已上线冻结模型（如推荐排序、商品OCR工具）可复用DEC的Decompose-Enhance-Correct三层Agent干预框架，无需重训即可优化长尾case效果，避免重新训练的高成本

  - 借鉴VC-Gate+VC-Ranker设计，用业务适配的无监督一致性信号（如推荐场景的点击一致性、OCR场景的视觉一致性）做干预触发和候选结果校验，降低bad
  case率

  - 构建业务长尾难例集时，可复用跨模型共识筛选策略，无需大量人工标注即可得到高质量的难例样本，用于专项优化或评估

  - 处理大尺寸输入（如长商品参数表、长用户行为序列）时，采用结构感知的拆分策略替代一刀切的截断/缩放，减少信息损失'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有主流表格解析器在公开基准上TEDS得分超93，但真实场景下的复杂表格（大尺寸表、无框表、低质模糊表等）仍存在大量识别错误，聚合评估指标掩盖了实际性能缺陷；同时通过重训修复长尾问题需要大量标注、算力，且无法适配封闭源/已上线的冻结模型，亟需低成本的优化方案和细粒度的问题诊断工具。
### 方法关键点
- 构建TableParseMap诊断基准，包含916个真实复杂表格，覆盖5种难例场景、9类解析错误，可细粒度定位解析器的能力短板
- 提出DEC Agent框架，无需重训底层冻结解析器：Decompose按结构安全边界拆分大表，Enhance用图像工具强化弱视觉线索后重解析，Correct基于渲染结果与原图的一致性诊断修复残留错误
- 设计VC-Gate触发干预、VC-Ranker做候选结果校验与回退，推理阶段无需真值标签即可实现可靠的性能提升
- 提出跨模型共识筛选策略，从4556个候选样本中自动筛选出1977个多模型均难以处理的Consensus-Hard难例集，可用于专项评估
### 关键实验
在3个主流冻结表格解析器上测试，DEC平均提升TEDS 1.57点；在TableParseMap基准上整体TEDS提升1.89点，结构类错误提升2.62点，大表场景提升5.66点；VC-Gate仅需触发43%的请求即可保留97.5%的性能增益，额外解析调用量减少47.3%。
### 核心结论
对于已部署的冻结模型，用轻量Agent做推理时分层干预，配合无监督一致性校验，是低成本提升长尾case效果的有效路径。
