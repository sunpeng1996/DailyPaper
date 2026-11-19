---
title: 'Ground, Iterate, Trace: Decomposing AI Research Ideation'
title_zh: 可追溯科研创意生成Agent框架CAR：知识图谱+显式创意算子
authors:
- Samson Yu
- Qiran Zou
- Jing Yu Lim
- Rushi Shah
- Anirudh Goyal
- Dianbo Liu
affiliations:
- National University of Singapore
- Meta Superintelligence Labs
arxiv_id: '2611.24887'
url: https://arxiv.org/abs/2611.24887
pdf_url: https://arxiv.org/pdf/2611.24887
published: '2026-11-18'
collected: '2026-11-19'
category: Agent
direction: Agent 可追溯科研创意生成框架
tags:
- Ideation Agent
- Knowledge Graph
- Creative Operator
- Traceable Reasoning
- LLM4Science
one_liner: 提出融合文献知识图谱与四种显式创意算子的可追溯科研创意生成Agent，兼顾新颖性与可行性
practical_value: '- 四种创意算子可直接迁移到电商推荐/营销创意场景：bisociate算子跨域关联不同品类特征生成跨界推荐/联名活动思路，analogy算子将成熟品类运营方案迁移到新品类，降低创意试错成本

  - 「知识图谱接地+算子调用校验+全链路追溯」的架构可复用在生成式推荐/营销文案生成流程中，每一步生成都校验合规性，所有输出可追溯到原始商品/用户/案例数据源，解决生成内容的侵权、合规、归因问题

  - 迭代生成的设计可优化现有生成式推荐的prompt工程：将单次生成拆分为多轮创意细化步骤，每轮仅完成一个算子对应的修改，相比单次长篇prompt生成的内容稳定性更高、可控性更强'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM科研创意生成系统存在两极分化问题：激进prompt生成的创意新颖性高但可行性差，端到端AI科学家系统生成的创意可行性高但新颖性不足；且生成过程为黑盒，无法追溯创意与现有文献的关联，也难以拆分各个模块对最终创意质量的贡献，亟需兼顾新颖性、可行性且过程可追溯的创意生成框架。
### 方法关键点
- Ground阶段：针对给定主题检索最多20篇高相关文献，抽取问题、方法、结果、局限性等typed实体及关联关系，构建语义知识图谱，修复实体对齐与关系缺失问题后冻结作为创意生成的基础
- Iterate阶段：创意Agent可调用知识图谱检索工具，使用四种显式创意算子（bisociation跨域关联、analogy类比迁移、exploration边界探索、elaboration细节打磨）编辑图谱，每个算子调用前需通过结构化条件校验，不符合规则则返回错误提示要求Agent修正
- Trace阶段：全程记录所有算子的调用状态（成功/失败）、入参、关联的文献实体，最终输出的创意自带完整来源追溯链，所有引用的文献节点均可定位到原始来源
### 关键结果
在40个LiveIdeaBench跨领域主题上测试，对比单轮prompt、The AI Scientist、Research Ideation Agent（RIA）等基线，双骨干测试结果：方法学新颖度（MN）比单轮prompt高1.27（GPT-5.4）/1.87（GLM-5.2），比The AI Scientist高0.82/0.58；与RIA的MN无显著差异，但可行性得分高0.6/1.19；在FML-bench-Lite和BioXArena两个执行基准上，共用相同执行器的条件下，CAR的pairwise win rate分别达75%和64.8%，为所有对比AI方法最高。
### 核心结论
显式创意算子带来的可追溯性收益远大于其对创意质量的边际提升，在需要合规、归因的生产场景中，可追溯的迭代生成架构比黑盒一次性生成的落地价值更高
