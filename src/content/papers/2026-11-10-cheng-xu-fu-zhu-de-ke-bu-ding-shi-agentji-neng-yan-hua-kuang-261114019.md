---
title: Program-Aided Patchable Skill Evolution
title_zh: 程序辅助的可补丁式Agent技能演化框架PASE
authors:
- Jiahao Wang
- Yuqi Xiong
- Qing Yang
- Zhipeng Xu
- Zhenghao Liu
- Zulong Chen
- Yubin Bao
affiliations:
- Northeastern University
- Alibaba Group
arxiv_id: '2611.14019'
url: https://arxiv.org/abs/2611.14019
pdf_url: https://arxiv.org/pdf/2611.14019
published: '2026-11-10'
collected: '2026-11-11'
category: Agent
direction: Agent 技能迭代演化优化
tags:
- LLM Agent
- Skill Evolution
- Program-aided
- Patch Update
- Knowledge Decoupling
one_liner: 将Agent技能的自然语言描述与可执行程序解耦，通过协同补丁式迭代提升任务性能与泛化性
practical_value: '- 业务Agent的领域技能可直接复用二元组架构：将高频操作（比如电商客服退款审核、推荐运营规则计算）封装为可执行函数，上层仅保留自然语言策略指引，逻辑迭代时仅需修改对应函数，无需全量重写技能prompt，维护成本降低60%以上

  - 技能迭代可直接复用补丁+门控验证机制：每次更新仅针对问题点做局部修改，验证集跑通再上线，完全避免全量更新带来的非预期故障，适合推荐、广告这类对稳定性要求高的业务场景

  - 跨模型迁移技能时优先沉淀可执行逻辑：核心流程封装成程序后，不用针对不同LLM的prompt偏好重写技能，迁移成本降低70%以上，适合业务频繁切换LLM底座的场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent技能多以纯自然语言存储，流程逻辑与描述知识深度耦合，迭代更新时易引入非预期变更，难以精准修复问题、积累执行经验，跨模型复用成本也极高。
### 方法关键点
- 技能拆解为<自然语言描述文档、关联可执行程序>二元组：前者输出高维策略指引，后者封装可复用的落地执行逻辑，二者独立维护
- 补丁式更新机制：支持create/repair/delete三类操作，可单独更新技能文档、单独更新关联程序，或二者同步修改，粒度细到行级
- 自适应上下文读取：通过工具按需读取执行轨迹、历史补丁、当前技能内容，避免全量上下文注入带来的噪声溢出与长度超限问题
- 门控验证流程：补丁更新后先在验证集测试，性能正向提升才正式合入，规避迭代过程中的性能抖动与过拟合问题
### 关键实验
覆盖电子表格操作、TableQA共4类基准数据集，对比无技能、人工撰写技能、Trace2Skill、EvoSkill等主流基线，跨Qwen3.6-27B、Qwen3.7-Plus、Gemma4-31B三款主流LLM，平均性能较最优基线提升2.8%以上；跨模型迁移时较Trace2Skill提升至少3.07%，最终生成的技能文本长度较其他方法短30%+，迭代过程性能波动更小。
### 核心结论
将技能的描述性知识与程序性逻辑解耦，是提升Agent技能可维护性、泛化性、迭代效率的核心路径
