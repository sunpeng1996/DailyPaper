---
title: 'Skills Are Not Islands: Measuring Dependency and Risk in Agent Skill Supply
  Chains'
title_zh: Agent技能供应链的依赖关系与风险度量方法
authors:
- Changguo Jia
- Tianqi Zhao
- Runzhi He
- Minghui Zhou
affiliations:
- Peking University
- Zhongguancun Laboratory
arxiv_id: '2607.01136'
url: https://arxiv.org/abs/2607.01136
pdf_url: https://arxiv.org/pdf/2607.01136
published: '2026-07-01'
collected: '2026-07-02'
category: Agent
direction: Agent技能供应链治理与风险分析
tags:
- Agent Skill
- Supply Chain
- SBOM
- Dependency Analysis
- Security Risk
one_liner: 提出Agent技能供应链模型与SDA分析工具，精准识别跨技能/包/服务的依赖与安全风险
practical_value: '- 电商/推荐场景的自研Agent系统（如智能运营、客服Agent）可复用SDA的依赖分析框架，对技能库做全链路梳理，规避隐性依赖导致的线上故障、权限泄露问题

  - 内部Agent技能平台的建设可参考SkillBOM规范，强制要求技能提交时显式声明技能/软件包/第三方服务三类依赖，配套实现依赖冲突检测、风险审计能力

  - 安全风控流程可借鉴论文的传递性风险识别方法，对Agent技能做全链路扫描，检出仅检查单技能无法发现的恶意代码、数据泄露等传导风险'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
LLM Agent可复用技能规模3个月增长9倍至143万，但依赖关系隐式散落在元数据、自然语言指令、代码脚本中，缺乏统一管理机制，导致依赖冲突、版本丢失、安全风险传递等问题频发，传统面向软件包的SBOM工具无法适配技能的混合结构依赖分析需求。
### 方法关键点
- 提出Agent Skill Supply Chains（ASSCs）模型，用有向图统一建模技能、软件包、外部服务三类节点及对应的依赖关系
- 开发SkillDepAnalyzer（SDA）工具，通过结构感知解析提取元数据与依赖线索、证据校准分类高置信度依赖、增量递归解析传递依赖三个步骤，输出兼容现有SBOM标准的SkillBOM格式
- 构建人工标注的SKILL-DEP基准，覆盖单层依赖提取、多层依赖图构造两类评测场景
### 关键结果
- 评测阶段：SDA在SKILL-DEP基准上单层依赖提取F1达0.95，元数据提取准确率1.00，大幅优于传统SBOM工具（最高F1仅0.25）与DeepSeek-v4-pro基线（F1仅0.52）；多层依赖图构造F1达0.95
- 大规模分析阶段：对143万公开技能扫描发现，仅1.4%的技能显式声明依赖，71.87%的npm包、73.33%的PyPI包依赖为技能复用传递的隐性依赖，60%-98%的安全风险仅存在于传递性依赖中，单技能巡检完全无法覆盖

> 最值得记住的结论：Agent技能不是孤立个体，其依赖传递带来的隐性风险远高于显式风险，必须基于全链路供应链视角做治理。
