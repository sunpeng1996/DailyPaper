---
title: 'RubricAtlas: Mining Type-Level Rubrics from Expert Reports to Evaluate Deep
  Research Agents'
title_zh: RubricAtlas：从专家报告挖掘类型级规则以评测深度研究Agent
authors:
- Delin Wang
- Sinuo Wang
- Rui Sun
- Beidi Luan
- Qiming Shi
- Jing Li
- Daxin Jiang
- Zuo Bai
affiliations:
- StepFun
- FinStep
- Renmin University of China
- University of Adelaide
- Zhejiang University
arxiv_id: '2610.36878'
url: https://arxiv.org/abs/2610.36878
pdf_url: https://arxiv.org/pdf/2610.36878
published: '2026-10-27'
collected: '2026-10-28'
category: Agent
direction: 深度研究Agent · 自动化评测体系
tags:
- Research Agent
- LLM-as-a-Judge
- Rubric Evaluation
- Agent Evaluation
- Financial NLP
one_liner: 构建覆盖99类金融研究场景的类型级评估规则库，实现深度研究Agent的稳定可追溯评测
practical_value: '- 做Agent自动化评测时，可复用「类型级规则归纳+问题层级校验+证据关联」的框架，替代单任务人工写规则的模式，降低评测成本

  - 多源专家产出聚合时，可参考其“同类型下跨对象抽取共性分析要求”的方法，用于构建领域化评测标准（如电商品类分析报告的评测）

  - LLM-as-a-Judge落地时，可拆分「完整性校验（明确二元检查点）+ 有效性校验（单独规则）」的两段式设计，大幅提升评判一致性

  - 做长文本生成质量评估时，可借鉴其删除/padding扰动测试方法，验证评估指标是否不受无意义内容干扰'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有深度研究Agent的多步搜索+报告合成任务评测，多依赖单查询专属二元规则或单份参考报告，仅关注事实存在性，无法覆盖完整分析结构，且规则复用性差、评估结果受单份参考选择影响大，Agent排名稳定性不足，亟需可复用、可追溯、贴合专业要求的领域化评测体系。
### 方法关键点
- 类型级规则归纳：从同研究类型的多份专家报告中对齐共性分析问题，抽象为不绑定具体对象的评估要求，构建「维度→问题→目标→检查点」的层级规则树，区分共识（多数报告覆盖）和差异化（深度分析）问题赋予不同权重
- 证据关联评估：将报告段落与规则树对齐，检查点判定直接关联对应原文片段，单独计算分析完整性（仅校验要求内容是否存在）和论证有效性（单独校验逻辑缺陷），所有判定可追溯
- 抗干扰设计：每个目标设置负向判定准则，排除形似但不符合要求的内容（如用行业均值替代指定同行对比）
### 关键结果数字
- 基于3079份中文金融研报构建的RubricAtlas覆盖99类研究场景、921个分析问题、8160个检查点
- 单份专家报告平均仅覆盖同类型54%的分析问题，用单份报告的规则评测会使完整性得分虚高10.5分，与全库规则的Agent排名相关性仅Kendall τ=0.60
- 两个LLM评判管道的检查点一致性达Cohen's κ=0.71，Agent排名一致性达Kendall τ=0.87
- 针对性删除目标分析内容会使对应问题得分下降71%~83%，添加40%无关内容不会使评分显著上升
### 核心结论
领域Agent的长文本生成评测，基于多源专家共性归纳的类型级规则，远比单任务生成的规则更稳定、更贴合专业要求
