---
title: 'CUA-Universe: A Scalable and Dynamic Environment for Hybrid GUI+CLI Agents'
title_zh: CUA-Universe：支持GUI+CLI混合模式的可扩展计算机使用Agent环境
authors:
- Haoting Shi
- Wenhao Wang
- Weicheng Fang
- Yaozhong Liang
- Tian Jin
- Pengxiang Zhao
- Guangyi Liu
- Siheng Chen
- Yanfeng Wang
affiliations:
- Shanghai Jiao Tong University
- Zhejiang University
arxiv_id: '2609.05374'
url: https://arxiv.org/abs/2609.05374
pdf_url: https://arxiv.org/pdf/2609.05374
published: '2026-09-04'
collected: '2026-09-07'
category: Agent
direction: 计算机使用Agent · GUI+CLI混合交互
tags:
- ComputerUseAgent
- GUI-CLI-Hybrid
- Agent-Environment
- Task-Synthesis
- Trajectory-Generation
one_liner: 提出可扩展GUI+CLI混合Agent环境流水线，大幅提升计算机使用Agent的成功率与执行效率
practical_value: '- 业务Agent可复用多模态编排思路：将GUI可视化校验与CLI/API批量操作结合，比如电商商品上架Agent用GUI校验展示效果、用API做批量字段修改，大幅提升执行效率

  - 可复用Path-Steer轻量引导方案：仅给子任务的最优执行模态（GUI/CLI/API）先验，不用硬编码全流程，既降低推理成本又避免低效路径，适合电商运营、广告投放等固定流程多的场景

  - App-Forge环境构建思路可迁移：用Agent自动适配不同业务系统的API/CLI接口，无需人工逐系统做工具封装，快速搭建业务Agent的操作环境，降低接入成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有计算机使用Agent要么仅依赖GUI执行，路径冗长效率低；要么仅依赖CLI，缺乏视觉感知能力无法处理依赖界面状态的任务。同时混合GUI+CLI的环境构建依赖大量人工工程，可扩展性差，Agent也缺乏跨模态编排的训练数据，无法有效结合两种模态的优势。

### 方法关键点
- App-Forge：通过Agent自动将桌面应用适配为可复现的VM环境，自动发现、封装或生成对应CLI接口，无需人工逐应用开发，已支持16个跨领域桌面应用的GUI+CLI共享状态访问
- Task-Weave：从Agent探索轨迹中抽象可复用操作，基于种子文件组合生成难度可控的混合模态任务，通过Agent执行验证过滤不可行任务，形成持续的任务供给源
- Path-Steer：给Agent提供子任务最优模态先验引导（批量/精确操作用CLI，视觉相关操作用GUI），生成高效的混合执行轨迹，筛选高价值轨迹作为训练数据

### 关键实验
用生成的4923条混合轨迹做LoRA微调Qwen3.5-9B模型，在三个基准上取得提升：1）CUA-Verse基准：Score提升39.3pts，步骤减少37%，token减少60%，为当前最优开源结果；2）OSWorld基准：成功率提升16.8pts，步骤减少57%，token减少44%；3）OSWorld-MCP基准：Score提升7.84pts，步骤减少27%，token减少30%，跨工具接口的迁移能力显著。

> 最值得记住的一句话：比起单纯堆模型参数或者单模态训练数据，构建混合模态的可扩展环境与训练流水线，是提升计算机使用Agent能力与效率的更优路径。
