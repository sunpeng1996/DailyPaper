---
title: 'DocOps: A Verifiable Benchmark for Autonomous Agents in Complex Document Operations'
title_zh: DocOps：面向自主Agent复杂文档操作的可验证评测基准
authors:
- Jiazhen Jiang
- Boxi Cao
- Lingyong Yan
- Yaojie Lu
- Hongyu Lin
- Shuaiqiang Wang
- Dawei Yin
- Xianpei Han
- Le Sun
affiliations:
- 中国科学院软件研究所
- 中国科学院大学
- 百度 Inc.
arxiv_id: '2607.19865'
url: https://arxiv.org/abs/2607.19865
pdf_url: https://arxiv.org/pdf/2607.19865
published: '2026-07-21'
collected: '2026-07-23'
category: Agent
direction: Agent 文档操作能力评测基准
tags:
- Agent Benchmark
- Document Manipulation
- LLM Agent
- Deterministic Evaluation
- State Tracking
one_liner: 提出将文档作为一级状态对象的可验证Agent文档操作基准，揭示当前Agent能力边界
practical_value: '- 做电商运营/办公自动化Agent时，可复用三元谓词验证逻辑（结构谓词+语义锚+保留性检查），避免LLM-as-judge的不准确问题，尤其适合处理带公式的运营报表、商品详情页批量修改等场景

  - Agent执行框架选型参考：中小模型优先选择带文件系统反馈的harness（如Terminus-2）搭配针对性文档操作skill，性能远高于受限工具调用；前沿大模型skill增益有限甚至负向，优先选择开放编程环境

  - 处理强耦合文档（如多源数据汇总Excel、跨页面商品规格PDF）时，必须新增全局状态跟踪+结构校验模块，论文中80%以上多步任务失败来自状态丢失、浅语义校验、破坏性编辑三类问题，可针对性做容错'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agent文档操作基准要么仅关注只读文档理解，要么仅测试应用层流程编排，未将文档作为有状态的一级计算对象，无法验证Agent修改后文档的原生结构有效性、是否存在破坏性编辑，也无法细粒度定位失败根因，无法支撑高可靠办公自动化Agent的研发。

### 方法关键点
- 双轴任务分类体系：操作轴拆分出内容/格式/结构三类原子编辑能力，难度轴划分L1原子编辑到L4跨文档工作流4级复杂度，可直接定位Agent失败是来自局部操作错误还是全局状态丢失
- 确定性验证器：设计三类验证谓词，结构谓词检查公式、层级等原生文档状态，语义锚验证内容准确性，保留性谓词校验非编辑区域完整性，无需依赖LLM-as-judge，验证准确率达95.3%
- 构建210个覆盖XLSX/DOCX/PPTX/PDF四类主流格式的标准化任务，每个任务打包为可复现的Harbor包，包含源文件、指令、验证器

### 关键结果
测试12款主流开源/闭源模型+4种执行harness，最高配置（GPT-5.5+Codex+skill）总通过率仅67.1%，L4跨文档任务通过率暴跌至23.7%；强耦合的Excel类文档L3工作流通过率仅5.8%；70%以上的失败可归因为长期状态跟踪失败、浅语义校验、破坏性编辑三类模式。

**最值得记住的一句话**：执行框架对Agent文档操作性能的影响不亚于模型本身，长流程任务的核心瓶颈不是单步编辑能力，而是全局状态维护与结构语义校验能力
