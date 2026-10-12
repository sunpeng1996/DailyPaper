---
title: 'ProgramGym: Scaling Training Environments for Long-Horizon Program Reproduction
  Agents'
title_zh: 《ProgramGym：面向长程程序复现Agent的可扩展训练环境框架》
authors:
- Chengyi Yang
- Renxu Bao
- Jue Hou
- Zongpei Teng
- Ziheng Wang
- Yujie Lin
- Chengsong Huang
- Junnan Zhu
- Delai Qiu
- Yining Wang
affiliations:
- Xiamen University
- Washington University in St. Louis
- Institute of Automation, Chinese Academy of Sciences
- Unisound
arxiv_id: '2610.13395'
url: https://arxiv.org/abs/2610.13395
pdf_url: https://arxiv.org/pdf/2610.13395
published: '2026-10-08'
collected: '2026-10-12'
category: Agent
direction: 代码Agent · 长程任务训练与工作流优化
tags:
- CodingAgent
- LongHorizonTask
- TrainingEnvironment
- AgentWorkflow
- ProgramSynthesis
one_liner: 提出包含1648个可验证训练环境的ProgramGym框架与配套工作流，提升长程代码Agent程序复现性能
practical_value: '- 可复用Agent角色隔离工作流：将分析、实现、审核三个角色拆分到独立会话，用结构化交接文档传递信息，避免长上下文污染，适合电商Agent处理商品详情生成、活动规则落地等长程任务

  - 可复用反馈驱动的环境构建pipeline：用动态校验+失败诊断反馈循环批量生成可验证的训练环境，适合快速搭建推荐/广告Agent的离线仿真测试集，减少人工标注成本

  - 可复用版本管理+失败回滚机制：每轮迭代输出可独立构建的版本快照，失败自动回滚到上一有效版本，适合业务侧Agent的生产级稳定性保障，降低长程任务出错的影响范围'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有代码Agent多聚焦bug修复、单文件生成等短程任务，面向从零复现完整程序的长程场景存在两大核心痛点：一是缺乏可扩展、可验证的训练环境，现有框架要么依赖给定代码库/明确需求文档，要么缺少可靠的黑盒行为校验机制，无法提供有效的训练监督；二是通用单会话Agent工作流无法支撑长程开发，易出现上下文遗忘、提前终止、实现偏离需求等问题，性能瓶颈显著。
### 方法关键点
- **Program-Env**：通过反馈驱动的流水线批量生成训练环境，先从GitHub筛选3万+候选仓库，经在线依赖准备、离线编译校验生成可执行参考程序与网络隔离沙箱，再通过多模块并行测试生成+动态覆盖率反馈+四重用例校验，最终产出1648个覆盖C/C++/Go/Rust的高置信度训练环境
- **Program-Agent**：采用角色隔离的迭代工作流，拆分分析、实现、审核三个独立会话，分析阶段冻结需求证据、实现阶段仅基于交接文档开发、审核阶段对比参考程序输出可落地修改需求，搭配版本快照管理与编译失败自动回滚机制，保障长程任务稳定性
### 关键实验
在ProgramBench基准测试上：Qwen3.8-27B经Program-Env轨迹微调后测试通过率从34.87%提升至42.84%；搭配Program-Agent后，基础模型与微调模型通过率分别提升至55.71%、56.25%，超过Claude Opus 4.7等旗舰模型；迭代预算从1轮提升到5轮时，通过率从43.49%升至56.25%，性能随迭代次数持续增长。
### 核心结论
长程Agent的性能提升，70%来自合理的工作流设计与训练环境保障，30%来自模型本身的能力。
