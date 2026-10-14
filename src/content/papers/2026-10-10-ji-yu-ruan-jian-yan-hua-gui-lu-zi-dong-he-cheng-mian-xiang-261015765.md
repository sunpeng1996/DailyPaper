---
title: 'A Decade in a Day: Synthesizing Agent-Native Interfaces from Human-Oriented
  Software Evolution'
title_zh: 基于软件演化规律自动合成面向Agent的原生操作接口
authors:
- Alan Wu
- Wei Tao
- Yiwen Guo
affiliations:
- Independent Researcher
- LIGHTSPEED
arxiv_id: '2610.15765'
url: https://arxiv.org/abs/2610.15765
pdf_url: https://arxiv.org/pdf/2610.15765
published: '2026-10-10'
collected: '2026-10-14'
category: Agent
direction: Agent 工具调用接口优化
tags:
- LLM Agent
- Tool Calling
- Interface Synthesis
- Desktop Agent
- Benchmark
one_liner: 通过分析桌面软件演化规律，提出Agent友好接口三属性及合成框架ANIS，提升操作成功率降低token消耗
practical_value: '- 工具接口设计可复用三大核心原则：优先保证操作可发现性（配精简清晰的参数说明）、粒度匹配（将高频操作打包为原子命令）、可观测性（每个写操作配对应状态读取接口），可直接套用在电商运营Agent、广告投放Agent的工具封装环节，降低Agent出错率

  - 可复用token优化技巧：将高频多步操作序列封装为goal-level高阶命令，实测可降低73%左右的token消耗，同时提升成功率，适合迁移到业务Agent的工具层，降低推理成本

  - 无文档系统的工具接入可复用ANIS的能力收集方案：直接从运行时系统的注册接口、操作菜单、对象属性中爬取能力，经过有效性验证后生成工具列表，解决老旧业务系统无文档无法接入Agent的问题

  - 业务Agent提示词优化结论：给Agent提供完整官方文档无法稳定提效，反而会增加token消耗和干扰，优先提供精简的、经过运行时验证的工具说明即可'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前LLM Agent已成为桌面软件的新型使用者，但现有GUI、SDK、CLI接口均面向人类或开发者设计，Agent需额外消耗大量token解析视觉元素、组合底层调用，接口不匹配成为任务执行的核心瓶颈，此前缺乏对Agent友好接口属性的系统性研究。
### 方法关键点
- 构建DeskIF-Bench基准测试集：包含6款桌面应用、255个可通过最终产物自动验证的任务，采用控制变量法（固定Agent、任务、验证逻辑，仅更换软件版本）分析接口演化对Agent性能的影响
- 提炼Agent友好接口三大核心属性：可发现性（操作语义、参数清晰易查找）、粒度匹配（操作粒度对齐用户目标，减少底层调用）、可观测性（状态修改后有对应读取接口可验证效果）
- 提出ANIS接口合成框架：先从运行时应用的注册操作、对象属性、菜单三个来源收集能力，验证后生成统一格式的原子命令（每个写操作配对应读操作）；再从Agent执行轨迹中挖掘高频多步操作序列，验证可复现后封装为目标级高阶命令
### 关键实验结果
在扩展至8款应用368个任务的测试集上，对比原生SDK、CLI-Anything两个基线：
- ANIS原子命令层相对原生SDK，成功率提升3.8（DeepSeek V4 Flash）/3.5（Claude Haiku 4.5）个百分点，token消耗降低约73%
- 叠加目标级命令后，成功率进一步提升至74.5%（DeepSeek）/67.4%（Claude），相对CLI-Anything提升超57个百分点
- 禁用可观测性读命令会导致成功率下降12个百分点；给Agent提供完整官方文档反而平均降低成功率1~2个百分点，同时增加20%以上的探索类token消耗
### 核心结论
Agent的接口设计是独立于Agent本身能力的核心影响因素，无需等待软件厂商适配，通过自动合成即可快速得到Agent友好的操作接口。
