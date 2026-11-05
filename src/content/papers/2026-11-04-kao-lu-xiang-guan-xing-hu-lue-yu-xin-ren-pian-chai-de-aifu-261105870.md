---
title: AI-Assisted Classification under Correlation Neglect and Trust
title_zh: 考虑相关性忽略与信任偏差的AI辅助分类决策框架
authors:
- Dingwen Kong
- Liang Lyu
- Saurabh Amin
- Amine Bennouna
- Daniel Huttenlocher
- Asuman Ozdaglar
affiliations:
- MIT
- Northwestern University
arxiv_id: '2611.05870'
url: https://arxiv.org/abs/2611.05870
pdf_url: https://arxiv.org/pdf/2611.05870
published: '2026-11-04'
collected: '2026-11-05'
category: Other
direction: 人-AI协同决策 · 行为建模与部署优化
tags:
- Human-AI Collaboration
- Behavioral Modeling
- Decision Making
- Trust Calibration
- Classification
one_liner: 构建人-AI协同分类行为模型，给出AI能力与信息重叠维度的性能相图与部署策略
practical_value: '- 做电商内容审核、商品打标等人-AI协同场景时，不要盲目投入资源提升AI standalone准确率，优先评估AI输出与运营人员判断的信息重叠度，重叠过高时AI增加的新信息不足以抵消人类重复计数的偏差，反而拉低整体准确率

  - 不同能力的AI匹配不同信任引导策略：强AI（如GPT-4o级别的违禁内容识别模型）可通过运营培训提升对AI输出的信任，接近AI单独准确率；弱AI（如小模型的标签推荐）仅作为辅助参考即可，强行要求运营采纳反而会降低效果

  - 人-AI协同场景可复用三相图框架做部署决策：AI能力极弱时不提供辅助，中等能力时做互补推荐，能力超过阈值时直接自动化，无需走人类复核流程，降低运营成本

  - 训练面向人工复核的辅助大模型时，可针对性优化模型输出人类容易漏判的特征（如冷门违规内容、小众商品属性），降低信息重叠度，无需提升AI单独准确率即可提升人-AI团队的整体表现'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有人类-AI协同效果差异极大，部分场景AI能大幅提升决策准确率，部分场景反而拉低整体表现，过往研究仅关注AI单独准确率，忽略了AI与人类的信息重叠度、人类决策的行为偏差两个核心变量，既无法解释不同场景的效果差异，也缺乏可落地的部署指导。
### 方法关键点
- 构建双参数人类行为模型：用**相关意识α**衡量人类对AI与自身信息重叠的感知程度（α=0为完全相关性忽略，将重叠信息视为独立新信息），用**信任β**衡量人类对AI输出的决策权重（β<1为信任不足，β>1为过度信任）
- 定义重叠系数λ：AI掌握的证据中人类已掌握的比例，作为场景固有参数
- 推导闭形式三相图：以AI能力τA、重叠系数λ为维度，划分三个性能区域：互补区（人-AI团队准确率最高）、受损区（人类单独决策准确率更高）、自动化区（AI单独决策准确率最高）
- 损失拆解：将人-AI团队相对贝叶斯最优的准确率损失拆分为相关性忽略成本、信任不足成本，分别对应AI侧降低重叠、人类侧校准信任两个独立优化杠杆
### 关键实验
在ChatBench数据集（643名标注员回答MMLU多类目选择题，分别搭配GPT-4o、Llama-3.1-8b做AI辅助）上验证：
- 整体AI辅助让准确率从0.612提升到0.824，涨幅21个百分点，但人类仅给AI输出约1/4的贝叶斯最优权重（β=0.285）
- GPT-4o属于自动化区，AI单独准确率0.884高于团队的0.851，校准信任可提升团队准确率2.6个百分点；Llama-3.1-8b处于互补/自动化边界，校准信任反而会降低准确率1.4个百分点
### 核心金句
人-AI协同的效果不取决于AI单独准确率，而是由AI能力、AI与人类的信息重叠度、人类的行为偏差共同决定，盲目提升AI能力或校准信任都可能适得其反
