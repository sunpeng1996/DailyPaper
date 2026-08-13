---
title: 'SkillZip: Contract-Preserving Graph Compression for Scalable Agent Skill Libraries'
title_zh: SkillZip：面向可扩展Agent技能库的合约保留图压缩方法
authors:
- Xingyu Tan
- Xiaoyang Wang
- Qing Liu
- Xiwei Xu
- Xin Yuan
- Liming Zhu
- Wenjie Zhang
affiliations:
- UNSW
- CSIRO
arxiv_id: '2608.05604'
url: https://arxiv.org/abs/2608.05604
pdf_url: https://arxiv.org/pdf/2608.05604
published: '2026-08-05'
collected: '2026-08-13'
category: Agent
direction: Agent技能库 · 图压缩优化
tags:
- Agent Skill Library
- Graph Compression
- Procedural Memory
- Skill Retrieval
- LLM Agents
one_liner: 提出面向可扩展Agent技能库的合约保留图压缩框架SkillZip，兼顾高压缩比与执行可靠性
practical_value: '- 对于电商/广告Agent的运营、客服、工具类技能库，可复用段级拆分思路，将整包技能拆分为意图、操作、校验、输出等可复用单元，减少冗余context加载

  - 技能压缩不要仅依赖文本摘要，必须保留前置条件、依赖关系、校验逻辑三类核心合约信息，避免压缩后技能执行出错

  - 增量更新技能库时，可复用ReZip的反馈机制，基于执行失败、人工修正的trace动态调整压缩宏的粒度，平衡压缩率和准确率

  - 技能检索不要以完整技能包为最小单位，可融合段级语义匹配和技能级RRF排序，兼顾召回精度和上下文连贯性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent技能库规模快速扩张，现有方案以整包为检索单位、仅做文本压缩，存在粒度太粗浪费context、压缩丢失执行依赖/校验规则导致执行出错、压缩结构无法持久复用、难支持技能增量更新四大问题，无法在有限context窗口下暴露最小可用的执行上下文。

### 方法关键点
- Sec2Graph：将每个技能包拆分为带执行角色（意图/输入/操作/校验/输出等）的段级节点，构建带依赖、归属、等价关系的统一技能图，暴露跨技能的可复用单元
- MotifZip：挖掘频繁出现的符合合约要求的子图结构，替换为可逆向展开的宏节点，要求保留边界签名、依赖闭合、校验可达性三个约束，避免丢失执行关键信息
- PathHydrate：查询时先做双级种子融合（段级匹配+技能级RRF排序），再搜索满足依赖闭合、校验可达的最小子图，按需展开宏节点生成最小可用执行上下文
- ReZip：基于新增技能和执行trace增量更新压缩图，复用已有宏，新增高频有效子图为宏，降级高风险宏

### 关键实验
在SkillsBench、ALFWorld两个基准测试，对比Vanilla Skills、SkillDAG等基线，MiniMax-M2.7下ALFWorld成功率比最强基线SkillDAG高12.2个点，SkillsBench奖励高6个点；实现3.46×压缩比，依赖保留率99.2%，校验可达率98.7%，技能库从200扩容到100K仍保持稳定检索效果。

最值得记住的一句话：技能压缩的核心不是单纯缩短文本长度，而是要保留执行所需的完整合约信息，否则压缩率再高也没有实际业务价值。
