---
title: 'Dockerless: Environment-Free Program Verifier for Coding Agents'
title_zh: 面向编码Agent的无环境依赖代码补丁验证器Dockerless
authors:
- Wenhao Zeng
- Yuling Shi
- Xiaodong Gu
- Chao Hu
- Chaofan Wang
- Yuhao Cui
- Hongting Zhou
- Mengnan Qi
- Jianqiao Wangni
- Zhaojian Yu
affiliations:
- Shanghai Jiao Tong University
- Douyin Group
arxiv_id: '2606.28436'
url: https://arxiv.org/abs/2606.28436
pdf_url: https://arxiv.org/pdf/2606.28436
published: '2026-06-25'
collected: '2026-07-01'
category: Agent
direction: 编码Agent · 无环境依赖验证
tags:
- Coding Agent
- Reward Model
- SFT
- RL
- Static Verification
one_liner: 提出无环境依赖的代码补丁验证器，支持编码Agent全流程无Docker的SFT与RL训练
practical_value: '- 做业务Agent的奖励模型时，可复用「生成多维度验证问题→子Agent并行检索上下文收集证据→综合判分」的架构，比如电商活动策略、营销文案生成后的正确性核验，无需真上线就能低成本获取反馈信号

  - SFT训练数据筛选场景，可参考用验证器替代真实执行标注的思路，比如推荐系统用户仿真交互轨迹、Agent客服应答轨迹的质量过滤，大幅降低标注和环境搭建成本

  - 对合规要求高、无法搭建完备测试环境的业务场景（比如金融级推荐、敏感场景Agent），这种无环境、基于上下文证据的验证范式可直接复用，降低测试风险'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前编码Agent的SFT轨迹筛选、RL奖励计算都依赖在Docker环境中执行单元测试验证代码补丁正确性，单仓库环境搭建成本极高，大量私有、遗留代码库没有可复现的执行环境，现有无环境验证器仅做表面文本匹配，准确率不足以支撑复杂任务。
### 方法关键点
- 架构分两阶段：首先基于issue和参考补丁生成2-4个多维度验证问题（覆盖补丁位置、预期行为、测试证据、边缘case），再调度并行子Agent通过只读shell工具探索代码库收集每个问题的证据，最终综合所有证据输出补丁正确性分数
- 训练采用拒绝采样，仅保留最终判决与执行ground truth一致的问答轨迹，同时控制正负样本比缓解类别不平衡
- 可同时作为SFT轨迹过滤器与RL奖励信号，实现编码Agent全流程无Docker环境的后训练
### 关键结果
- 验证器层面：在SWE-bench Verified、Multi-SWE-bench Flash上AUC分别达81.0、72.1，比最强开源验证器基线高14.3、9.2个点
- Agent训练层面：全流程无环境训练的9B模型在SWE-bench Verified、Multilingual、Pro上resolve率分别达62.0%、50.0%、35.2%，超出Qwen3.5-9B基线2.4、8.7、2.9个点，性能与依赖环境的训练效果持平

最值得记住的一句话：基于主动探索和证据的Agentic验证范式，可大幅降低Agent训练对真实执行环境的依赖，为长尾、受限场景的Agent落地提供了可扩展的可行路径
