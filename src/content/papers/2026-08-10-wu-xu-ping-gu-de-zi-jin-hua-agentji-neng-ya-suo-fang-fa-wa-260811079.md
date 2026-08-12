---
title: 'SkillZip: Evaluation-Free Skill Compression for Self-Evolving Agents by Discovering
  Reusable Structure'
title_zh: 无需评估的自进化Agent技能压缩方法SkillZip：挖掘可复用结构
authors:
- Xiaofan Bai
- Hongqiang Lin
- Chao Liu
- Yantao Zhang
- Xuan Jin
- Xipeng Cao
- Yuhong Li
affiliations:
- Alibaba Group
- Zhejiang University
- Duke University
arxiv_id: '2608.11079'
url: https://arxiv.org/abs/2608.11079
pdf_url: https://arxiv.org/pdf/2608.11079
published: '2026-08-10'
collected: '2026-08-12'
category: Agent
direction: 自进化Agent · 技能压缩优化
tags:
- Self-Evolving Agent
- Skill Compression
- MDL
- Prompt Optimization
- Context Efficiency
one_liner: 通过结构化知识归并实现无评估Agent技能压缩，降本同时保留规则完整性
practical_value: '- 电商智能导购、客服、运营自动化等自进化Agent的技能迭代场景，直接接入Zip-on-Write模式从迭代初期开启压缩，可降低30%+技能token成本，同时避免大促规则、异常兜底等罕见规则丢失

  - 自迭代推荐策略Agent（如自动优化召回规则、商品文案生成规则的Agent）可复用其结构化契约解析+MDL优化逻辑，替代通用prompt压缩方案，避免破坏规则的作用域、依赖约束

  - 跨模型部署Agent技能时，用SkillZip压缩后的技能显式保留所有规则、输出schema，跨模型性能保留率可达97%，无需针对每个目标模型重新适配技能'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
自进化Agent会持续将成功执行流程、失败修复逻辑追加到技能prompt中，迭代5轮后技能长度平均膨胀到初始的5.2倍，重复规则、重复流程占比极高，既增加token调用成本，也会干扰LLM对核心执行逻辑的判断。通用prompt压缩方法依赖下游任务rollout验证，压缩成本高且容易丢失仅出现1次的关键边界规则（如电商大促特殊规则），无法适配自进化技能的高知识密度特性。
### 方法关键点
- 首先将非结构化技能文本解析为结构化契约，拆分为接口、工作流、工具协议、作用域规则、输出契约、支撑证据6类组件，解析置信度低的内容直接锁定、原样保留不参与压缩
- 基于最小描述长度（MDL）做优化，核心逻辑为「一次定义、多次引用」：重复规则上提至公共作用域、重复动作序列抽为共享子程序、仅保留差异化的例外规则，要求所有提取到的规则100%被覆盖
- 支持两种部署模式：one-shot模式单次压缩已有的成熟技能；Zip-on-Write模式在Agent每次技能更新时就地增量压缩，无需回溯全量历史数据
### 关键实验
在BFCL-v4网页搜索、LiveMath数学推理、SpreadsheetBench表格操作3个基准数据集上，对比SkillReducer等基线：
1. 平均压缩率达31.2%，是SkillReducer（9.2%）的3倍以上，压缩后任务性能持平甚至略高于原技能
2. 压缩速度比SkillReducer快3.5倍，全程不需要任何任务rollout验证
3. 跨模型迁移时性能保留率达97%，比基线高6个百分点
4. Zip-on-Write模式从迭代初期开启，可将最终技能长度控制在初始的1.6~1.9倍，比无压缩场景降低38%~50%的长度
### 值得记住的一句话
自进化Agent的技能冗余不是无用内容，而是重复的结构化表达，压缩应该做知识归并不是内容过滤
