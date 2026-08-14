---
title: 'MindMemOS: A Portable and Self-Evolving Memory Operating Layer for AI Agents'
title_zh: MindMemOS：面向AI Agent的可移植自进化记忆操作层
authors:
- Kaichao Liang
- Yuqi Cui
- Hao Kong
- Xinyuan Huang
- Guohaotian Hou
- Qingcan Kang
- Liang Chen
- Yiyang Yin
- Ke Ye
- Jiaquan Guo
affiliations:
- Noah's Ark Lab, Huawei Technologies
arxiv_id: '2608.12428'
url: https://arxiv.org/abs/2608.12428
pdf_url: https://arxiv.org/pdf/2608.12428
published: '2026-08-12'
collected: '2026-08-14'
category: Agent
direction: AI Agent · 长时记忆管理与自进化
tags:
- Agent Memory
- Long-term Memory
- Self-evolution
- Memory Consolidation
- Skill Evolution
one_liner: 提出具备自进化能力的AI Agent通用内存层，支持记忆自适应、自动巩固、技能迭代
practical_value: '- 可复用「实体-属性-时间」三维记忆结构搭建电商用户偏好记忆系统，解决多轮交互上下文遗忘、新旧偏好冲突问题

  - 离线Dreaming记忆巩固机制可直接迁移到用户行为日志清洗流程，自动合并冗余记录、压缩活跃存储，降低在线检索噪声

  - MindSkillEvolve轨迹转技能思路可用于导购Agent迭代，基于对话和成交轨迹自动优化导购话术、推荐逻辑

  - 隐式反馈记忆更新策略可用于推荐系统偏好感知，无需用户明确打分即可从接受/拒绝行为中更新用户画像'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Agent记忆系统要么与底座模型强绑定可移植性差，要么部署后记忆结构固定，无法自适应场景、自动处理冗余冲突，也难以将执行经验转化为可复用技能，限制了长周期交互下的个性化能力和任务成功率。

### 方法关键点
- 采用「实体-属性-时间」三维统一记忆结构，支持无建模引导的MindVanilla快速入库和schema引导的MindSchema结构化入库两种模式
- 核心进化机制包含4部分：1）MindMemEvolve用验证驱动的进化搜索自动适配场景化记忆schema；2）Dreaming离线合并冗余记忆、解决冲突，压缩活跃内存；3）显式+隐式用户反馈自动修正记忆偏差，区分临时指令和长期记忆；4）MindSkillEvolve从Agent执行轨迹中自动迭代优化可复用技能，支持无监督和带监督两种模式
- 检索层用稀疏+稠密混合匹配+双向图遍历的Compact Search，兼顾召回率和检索效率

### 关键实验
在LOCOMO长时对话记忆基准上，MindSchema模式整体准确率94.03%，超过SOTA基线EverOS 0.98个百分点；在PersonaMem用户个性化基准上整体准确率70.63%，超EverOS 3.06个百分点；Dreaming机制可提升整体记忆准确率最高8.2个百分点，同时压缩22.5%的活跃内存；MindSkillEvolve在SpreadsheetBench上较初始技能基线提升9.2个百分点的成功率。

**最值得记住的一句话**：Agent记忆系统的核心竞争力不止是存和取，更要具备自进化能力，才能适配开放场景下的长周期交互需求。
