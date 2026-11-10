---
title: 'InfraRSI: Harnessing Recursive Self-Improvement for Training Infrastructure'
title_zh: 《InfraRSI：基于递归自提升的分布式LLM训练基础设施优化Agent》
authors:
- InfraRSI Team
- Yuchuan Tian
- Haocheng Mei
- Ye Yuan
- Chao Xu
- Boxun Li
- Guohao Dai
- Kai Han
- Allen Chen
- Yunhe Wang
affiliations:
- Peking University
- TokenRhythm Technologies
- Infinigence AI
- Shanghai Jiao Tong University
- Tsinghua University
arxiv_id: '2611.11558'
url: https://arxiv.org/abs/2611.11558
pdf_url: https://arxiv.org/pdf/2611.11558
published: '2026-11-08'
collected: '2026-11-10'
category: Agent
direction: 训练基础设施Agent · 递归自提升
tags:
- Agent
- Recursive Self-Improvement
- LLM Training
- MoE
- Distributed Training
one_liner: 提出五阶段自提升Agent架构，联合优化训练配置与代码补丁，最高将LLM训练吞吐量提升2.75倍
practical_value: '- 做黑盒系统调优Agent时可复用「固定任务合约+多维度校验」机制，防止LLM奖励黑客（如调参时偷偷改模型结构/有效batch
  size造假），适合推荐/广告排序模型训练调优场景

  - 多起点初始化+全局执行时间/截尾内存模型的搜索框架，可直接迁移到GPU集群上的大模型召回/排序训练的超参、并行配置调优，避免OOM和局部最优

  - 跨硬件经验库的归一化存储+相似性检索机制，可复用在多机房/多GPU型号训练集群的调优经验沉淀，减少重复试错成本

  - 带失败归因的Bundle补全策略，适合多变量联合调优场景（如推荐系统召回+排序链路联合调优），不会因单个变量冲突放弃高收益组合'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
分布式LLM训练吞吐量受启动配置、算子内核、通信调度强耦合限制，直接用编码Agent或贪心搜索易出现奖励黑客、集群测量噪声、LLM先验失准、单起点搜索卡在OOM/编译悬崖四类问题，现有调优工具未覆盖配置与代码补丁的联合优化，也无法跨硬件迁移经验。

### 方法关键点
- 五阶段工作流：init锁定可编辑范围与任务合约（workload、loss、时序不变量）防奖励黑客；doctor采集基线、校准集群噪声；run联合优化启动配置与代码补丁，回溯重跑校验Top候选后写入跨硬件经验库；report与apply审计变更、核算试错成本、提交生效
- 预算组合搜索：多起点初始化（经验最优、LLM推荐、随机合法配置），拟合全局执行时间与截尾峰值内存模型（纳入OOM失败样本）；校准LLM失准先验，将高收益OOM配置与内存节省策略配对；高影响力旋钮逃逸+验证过的代码补丁堆叠，避免局部最优
- 跨硬件经验转移：将观测归一化为71种canonical机制，按硬件、workload相似性检索经验，冷启动搜索并初始化模型先验，避免跨GPU架构负迁移

### 关键结果
在4种单/多节点稠密、MoE LLM训练负载（Qwen3.5、Gemma-4等，H100/H200 GPU）上测试，对比OptiCo、Auto-Research、RE-Bench基线：几何平均吞吐量提升1.83倍，最高2.75倍；平均MFU从17.4%提升到30.0%；跨SKU经验转移可将Qwen3.5-9B调优收敛速度提升40%以上，最终吞吐量再提7%。

**最值得记住的一句话**：做系统级调优Agent的核心是把LLM生成能力和带校验的闭环搜索、可迁移结构化经验库结合，不能靠纯代码生成盲目试错。
