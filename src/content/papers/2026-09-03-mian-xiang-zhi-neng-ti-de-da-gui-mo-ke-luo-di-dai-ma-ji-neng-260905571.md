---
title: Grounded Skill Synthesis from Code at Scale for Agentic Intelligence
title_zh: 面向智能体的大规模可落地代码技能自动化合成框架
authors:
- Yongqi Tong
- Pan Wang
- Hang Wang
- Jianshe Li
- Xin Zhang
- Jiang-Ming Yang
- Wei Wu
affiliations:
- Ant International
arxiv_id: '2609.05571'
url: https://arxiv.org/abs/2609.05571
pdf_url: https://arxiv.org/pdf/2609.05571
published: '2026-09-03'
collected: '2026-09-21'
category: Agent
direction: 智能体技能库构建 · 代码知识蒸馏
tags:
- Agent Skill
- Code Mining
- Procedural Knowledge
- Skill Bank
- LLM for Agents
one_liner: 从大规模开源代码库自动化合成可落地可验证的技能库，大幅提升多场景智能体性能
practical_value: '- 做行业Agent时，可复用Code2Skill的「代码筛选-技能生成-盲重建校验」pipeline，从内部历史业务代码（如推荐特征工程脚本、活动规则执行代码）中蒸馏可复用的业务操作技能，降低Agent重复推理成本

  - 技能检索阶段可借鉴「skill summary 压缩」技巧，将长技能描述压缩为仅保留核心操作逻辑的短文本，降低88% context开销同时保留90%以上效用

  - 技能接入Agent工作流时优先选择规划阶段注入或生成后校验阶段注入，比直接拼接在生成prompt中效果更稳定，可显著提升业务Agent执行成功率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有智能体技能合成方法存在明显缺陷：轨迹派生的技能和生成环境、模型强绑定，质量受限于智能体自身能力上限；文档提取的技能缺乏可落地的执行证据，无法验证正确性。而GitHub等平台积累了海量经过实际调试、验证的代码，天然包含可复用的流程化知识，但缺乏高效的结构化提取方案。

### 方法关键点
- 提出Code2Skill全自动化pipeline：先从代码库筛选高复用价值的代码单元，按粒度抽象为原子操作、组合工作流、通用模式三类技能记录，每类记录包含适用场景、执行步骤、不变量、异常处理、来源证据等元信息
- 采用「源体盲重建校验」机制：仅用生成的技能记录让LLM重写代码，再和原代码做一致性比对，过滤不准确的技能，保证技能的可落地性
- 对19769个高星GitHub仓库执行pipeline，生成包含1006822条有效技能的CodeSkillBank，支持多维度高效检索

### 关键结果
跨9种模型、8个基准测试（含编程、科学推理、系统交互），接入CodeSkillBank的智能体平均性能相对提升11.7%，72组对比中57组优于基线；相比轨迹生成的技能库（Trace2Skill、ExpeL、SkillRL-Bank），CodeSkillBank在全部7个共享基准上表现更优，平均得分49.5，比最强基线高9.5分；从经过测试的AI生成代码中提取的技能通过率达93.5%，与人工代码提取的93%基本持平，支持技能库自动持续扩展。

**最值得记住的一句话**：从经过验证的代码中蒸馏的技能，比智能体自身交互积累的轨迹技能泛用性更强、提升更显著，是智能体能力规模化的新路径。
