---
title: 'JANUS: Enhancing Long-Horizon Autonomous Research with Co-Evolving World Models'
title_zh: JANUS：基于协同进化世界模型的长周期自主研究框架
authors:
- Mengdi Liu
- Chenghao Jia
- Hong Chang
- Mingjie He
- Shiguang Shan
- Xilin Chen
affiliations:
- Institute of Computing Technology, CAS
- University of Chinese Academy of Sciences
arxiv_id: '2610.13194'
url: https://arxiv.org/abs/2610.13194
pdf_url: https://arxiv.org/pdf/2610.13194
published: '2026-10-09'
collected: '2026-10-12'
category: Agent
direction: Agent 自主研究 · 世界模型协同进化
tags:
- Autonomous Agent
- World Model
- Co-evolution
- Long-horizon Planning
- Exploration Strategy
one_liner: 提出协同进化世界模型驱动的预测-验证-进化循环，大幅提升长周期自主研究效率与性能上限
practical_value: '- 做长周期推荐策略迭代/广告投放优化的Agent系统时，可复用价值提升+信息增益+探索效用三维打分机制，在AB实验前预筛候选策略，降低试错成本

  - 可借鉴进化研究图结构，统一管理历史实验、候选方案、路径依赖关系，解决策略迭代中的上下文漂移与信用分配问题

  - 多模块（如生成模块+评估模块）协同迭代的系统，可复用经验驱动的协同进化机制，分别蒸馏各模块的领域技能与协作规则，持续提升系统整体性能

  - 探索资源有限场景下，可借鉴动态权重调整的自适应探索策略，根据当前进度与剩余预算动态平衡短期收益与长期探索，提升资源利用率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有长周期自主研究采用Generate-Execute-Feedback范式，依赖反应式试错，执行成本高、反馈延迟大，搜索空间组合爆炸时进化效率极低，且容易提前达到性能天花板，无法适配高成本长周期探索需求。

### 方法关键点
- 构建**进化研究图**作为统一底座，动态记录候选方案、预估值、执行结果与路径依赖，支持分支探索、经验复用与拓扑感知性能归因
- 设计**Predict-Verify-Evolve**循环：预测阶段世界模型从价值提升、信息增益、探索效用三个维度对候选方案做稀疏成对tournament打分，预筛/修剪低价值分支，仅高价值方案进入执行；验证阶段落地执行获取真实反馈；进化阶段将反馈蒸馏为研究Agent分层技能、世界模型探索策略技能、两者协作协议三类，实现双模块协同进化
- 采用自适应权重调整机制，根据当前进度与剩余预算动态调整三个打分维度的权重，平衡短期收益与长期探索

### 关键结果
在MLS-Bench-Lite（30个跨领域ML研究任务）与3个真实研究任务（nanoGPT训练优化、MinGPT注意力核优化、基因型表型预测）上对比7个SOTA基线：1）同用DeepSeek-V4 Flash backbone时，MLS-Bench-Lite测试得分41.07，超过最强基线Codex的38.91；2）真实任务中平均样本效率比Codex高3.74倍，最高达43倍，进化天花板显著更高，基线进入平台期后仍能持续提升。

最值得记住的一句话：长周期探索系统的核心优化方向是从反应式试错转向元认知探索，通过先预测后执行、经验持续进化的机制，可同时提升进化效率与性能上限。
