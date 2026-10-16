---
title: 'HEM-Med: A Hierarchical Agentic Memory Framework for Safe Multi-Center Medication
  Recommendation'
title_zh: HEM-Med：面向多中心安全用药推荐的分层智能体记忆框架
authors:
- Min Xiao
- Jin Li
- Shoujin Wang
- Yeguang Zhen
- Yishuo Li
- Wenpeng Lu
affiliations:
- Qilu University of Technology (Shandong Academy of Sciences)
- University of Technology Sydney
arxiv_id: '2610.20191'
url: https://arxiv.org/abs/2610.20191
pdf_url: https://arxiv.org/pdf/2610.20191
published: '2026-10-14'
collected: '2026-10-16'
category: RecSys
direction: 多中心医疗推荐 · 智能体记忆与安全约束解码
tags:
- Multi-Center Recommendation
- Agentic Memory
- Knowledge Disentanglement
- Safe Recommendation
- Set Generation
one_liner: 提出分层智能体记忆框架，解耦跨院通用经验与院方处方偏好，结合安全解码提升多中心用药推荐效果
practical_value: '- 跨域/多中心推荐场景（如电商多站点、多业态推荐）可借鉴「通用共识经验+场景特异性残留记忆」的解耦架构，解决跨域负迁移问题，将通用用户偏好与站点专属运营规则拆分，避免跨域迁移效果下降

  - 组合推荐（如电商打包套餐、搭配推荐）可复用「候选召回+规则约束解码」的两阶段架构，将DDI互斥规则替换为业务互斥规则（如搭配禁忌、库存限制），在不损失召回准确性的前提下降低违规推荐比例

  - 记忆构建可引入「强记忆+加权弱记忆」的分级策略，弱记忆权重设置在0.4左右效果最优，兼顾长尾内容召回与噪声控制，适配冷启动、低资源场景的推荐系统'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有多中心用药推荐存在两大核心痛点：一是未将可迁移的通用临床经验与医院特异性处方偏好解耦，易引发负迁移，降低临床接受度；二是忽略药物互斥、本地处方目录等安全约束，难以落地。同时低资源医院数据稀疏，单中心模型效果差，跨院知识迁移的实际需求迫切。
### 方法关键点
- 构建L3级可解释患者用药-临床上下文归因记忆库，通过DeepSeek为每条用药记录匹配诊断、手术、异常检验指标等对应锚点
- 记忆解耦为两层：跨院共识记忆L1存储满足多院覆盖、高频出现的锚点-用药关联；医院特异性残留记忆L2存储与通用经验偏差超阈值的本地处方模式，同时保留弱记忆作为长尾场景补充，弱记忆权重固定为0.42
- 推荐分三阶段：从双层记忆召回Top60候选，经重排序校准得分后，通过DDI感知的集合解码优化全局目标，兼顾准确率、集合合理性、互斥风险、冗余度
### 关键实验结果
在eICU多中心数据集（9万+记录、149家医院）上对比10个主流基线，HEM-Med的PRAUC达0.4161，F1达0.4532，DDI率仅0.0831，综合SafeScore比最强基线SafeDrug高9.4%；消融实验验证所有核心模块均有显著收益。
### 核心结论
跨场景知识迁移的核心是先完成通用共识与场景特异性特征的解耦，再叠加业务规则约束，才能同时提升效果与落地可行性。
