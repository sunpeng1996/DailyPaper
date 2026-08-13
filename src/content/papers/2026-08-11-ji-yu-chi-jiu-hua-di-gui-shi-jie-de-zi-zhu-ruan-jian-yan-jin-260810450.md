---
title: Persistent Recursive Worlds Enable Autonomous Software Evolution
title_zh: 基于持久化递归世界的自主软件演进系统EvoX Genesis
authors:
- Beichen Huang
- Zhenyu Liang
- Bowen Zheng
- Ran Cheng
affiliations:
- The Hong Kong Polytechnic University
arxiv_id: '2608.10450'
url: https://arxiv.org/abs/2608.10450
pdf_url: https://arxiv.org/pdf/2608.10450
published: '2026-08-11'
collected: '2026-08-13'
category: Agent
direction: Agent 长周期任务协同优化
tags:
- Coding-Agent
- Multi-Agent
- Persistent-World
- Software-Evolution
- Long-Horizon-Agent
one_liner: 提出以持久化项目为核心的递归世界框架，实现低成本长周期自主软件演进
practical_value: '- 多Agent协同架构可直接复用：放弃维护持久化Agent身份/记忆，将项目（如推荐策略代码、特征工程脚本、营销文案库）的已验收版本、路径级上下文、约束、测试用例作为唯一持久化核心，大幅降低长周期多Agent任务的状态管理复杂度，适合推荐策略自动迭代、特征自动化开发等场景。

  - 递归任务拆分机制适配业务模块化场景：按业务模块（如商品模块、用户模块、排序策略模块）路径委派任务，父Agent仅负责校验结果、合并变更，子Agent负责具体执行，可直接用于电商商品详情页批量生成、营销文案分场景迭代、AB实验代码自动生成等场景。

  - 大模型调用成本优化trick：通过版本+路径维度的上下文缓存，实现96%+的输入token缓存命中率，大幅降低大规模Agent任务的调用成本，可复用到所有长周期多轮Agent、RAG类业务场景。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有长周期编码Agent依赖持久化的Agent会话、记忆或调度器实现连续性，当Agent替换、底层大模型更换时，任务难以平滑接续，且长周期运行的token成本极高，无法支撑跨周级别的复杂软件持续迭代。

### 方法关键点
- 定义持久化递归世界核心坐标为(已验收版本v, 仓库路径p)，所有代码、上下文、约束、测试用例、历史变更都存储在v中，Agent为临时生命周期，执行完单任务即销毁，私有状态不持久化。
- 递归委派机制：父Agent可在同一v下将子任务委派给更细路径q的子Agent，子Agent完成后返回变更，父Agent校验通过后才更新全局v，不通过则直接丢弃，不影响主版本状态。
- 验收准入机制：只有通过测试、符合约束的变更才会进入持久化版本历史，有价值的失败信息可存入上下文供后续Agent参考，避免重复踩坑。

### 关键结果
- 从空仓库生成24.9万行Rust实现的C编译器，耗时123.4小时，调用DeepSeek V4 Flash仅花费44.38美元，100%通过c-testsuite、93/93 Csmith测试。
- 支持跨大模型接续开发：GLM 5.2生成的编译器切换为DeepSeek V4 Flash后可继续迭代，测试通过率无损失，无需重新开发。
- 13.9万行Fortran实现的MESA科学计算模块重写为Rust，耗时33.2小时，花费10.64美元，数值误差小于1e-8，运行速度提升1.55~6.87倍。

### 核心结论
长周期智能任务的核心持久化对象不应是Agent本身，而是任务的状态、约束与验收标准。
