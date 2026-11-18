---
title: Self-Improvement Memory Enables Continual Recursive Self-Improvement
title_zh: 自优化记忆（SIM）实现Agent持续递归自提升
authors:
- Xin Yu
- Fei Xia
- Jiaqi Pan
- Youbao Tang
- Chengzhi Liu
- Adams Yu
- Sicong Jiang
- Yanfei Chen
- Lingzhou Xue
- Ting Yu
affiliations:
- Google Cloud AI
- Google DeepMind
- Google Cloud AI Research
- The Pennsylvania State University
arxiv_id: '2611.18856'
url: https://arxiv.org/abs/2611.18856
pdf_url: https://arxiv.org/pdf/2611.18856
published: '2026-11-12'
collected: '2026-11-18'
category: Agent
direction: Agent自优化 · 记忆机制设计
tags:
- Self-Improvement
- Agent Memory
- Recursive Self-Improvement
- Continual Learning
- Harness Optimization
one_liner: 提出结构化自优化记忆SIM，支撑Agent在基准/模型变更后持续优化harness，性能显著优于基线
practical_value: '- 可复用SIM的结构化记忆设计：将过往harness（提示词、工具链、执行流）的修改根因、预期/实际效果、部署上下文按问题聚类，避免跨场景/模型迭代时重复踩坑，适配电商Agent跨类目、大模型版本迭代的场景

  - 跨模型/跨场景harness迁移可直接套用CRSI框架：无需冷启动优化harness，保留SIM历史的迁移比仅迁移harness平均高2.36个点，可用于推荐系统Agent从通用场景到垂类场景的快速适配

  - Agent自优化流程可参考「提案-评估-选择」闭环搭配记忆机制：每次优化仅记录生效的修改及效果，平衡记忆存储成本和迭代效率，适合业务中频繁迭代的导购、客服Agent的自动优化'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前Agent的递归自提升（RSI）通常在固定基准、固定模型下优化管理上下文、工具、执行流的harness，一旦更换任务场景或升级基座模型，仅迁移优化好的harness会出现适配性下降，甚至表现不如初始种子harness；且过往优化历史丢失会导致迭代时重复尝试无效修改、不清楚原有修改的设计意图，跨场景迭代效率极低。
### 方法关键点
- 定义持续递归自提升（CRSI）场景：分为跨数据集（模型固定、基准变更）和跨模型（基准固定、模型变更）两类，全程保留harness的可执行接口不变
- 设计自优化记忆SIM：按harness的问题根因聚类存储每一次生效修改的内容与rationale、预期/实际任务效果、所属领域/基准/模型/迭代轮次等上下文信息
- 迭代流程优化：harness优化的提案器、选择器每轮迭代读取全部SIM内容，提案需关联已有根因或新建根因，每轮仅将选中的修改（含产生负向效果的失败修改）更新到SIM中
### 关键结果
在编码、文本分类、工作空间、工程设计4个领域测试，对比冷启动、仅迁移harness、仅存储根因3类基线：
- 6个跨数据集场景中SIM全部最优，较仅迁移harness高2.43~4.35个点；4个跨模型（Claude Opus到Gemini）场景全部最优，较仅迁移harness高3.60~11.33个点
- 10组独立编码任务配对实验显示，带SIM的迁移较仅迁移harness平均提升2.36个点（p=0.003），90%的场景下效果更优

> 最值得记住的一句话：迁移Agent的优化经验比仅迁移优化后的产物更能支撑跨场景持续迭代
