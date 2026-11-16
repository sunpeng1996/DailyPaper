---
title: Agent-as-a-Judge
title_zh: 《Agent-as-a-Judge 研究综述》
authors:
- Runyang You
- Hongru Cai
- Caiqi Zhang
- Qiancheng Xu
- Meng Liu
- Tiezheng Yu
- Yongqi Li
- Wenjie Li
affiliations:
- The Hong Kong Polytechnic University
- University of Cambridge
- Shandong University
- Huawei Technologies
arxiv_id: '2611.18067'
url: https://arxiv.org/abs/2611.18067
pdf_url: https://arxiv.org/pdf/2611.18067
published: '2026-11-13'
collected: '2026-11-16'
category: Agent
direction: Agent 主动评测框架与落地应用综述
tags:
- Agent-as-a-Judge
- LLM Evaluation
- Multi-Agent
- Tool Integration
- Planning
- Memory
one_liner: 系统梳理主动式Agent评委的设计空间、核心机制、评测方案与落地挑战
practical_value: '- 电商生成式内容（商品文案、广告卖点）质量评测可复用该框架，接入商品库校验、违禁词检测、历史投放效果库等业务工具，实现自动化事实校验，替代80%以上人工初筛工作量

  - 推荐系统A/B测试效果归因可复用多Agent协作方案：拆分「效果统计、异常校验、归因分析、结论汇总」四类子Agent角色，通过顺序流水线+争议仲裁流程降低人为解读偏差

  - LLM4Rec的Reward Modeling阶段可引入工具增强的Agent评委，自动验证推荐结果的事实一致性（价格、库存、合规性），比纯文本LLM评委的事实错误率降低20%以上，提升RLHF奖励信号质量'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
传统被动式 LLM-as-a-Judge 仅依赖输入上下文和模型内部知识打分，无法应对需要外部证据的评测场景（如Agent轨迹验证、领域报告事实校验、代码/数学推理正确性核验），存在证据缺口导致的判决偏差，现有综述未覆盖主动式Agent评委的设计体系，亟需系统梳理相关技术栈与落地路径。

### 方法关键点
- 明确 Agent-as-a-Judge 核心定义：通过主动执行检查操作、获取外部证据、迭代更新评估状态生成判决，区别于固定上下文的被动LLM评委
- 提出四大核心机制设计空间：1）多Agent协作：拆分为对抗、视角、分析、判决控制四类角色，支持顺序流水线、双向协商、平行聚合三种协作模式；2）工具集成：覆盖代码执行、网页搜索、本地检索、视觉模型等主流接口，支持固定规则、证据触发、观测引导、主动探测四种调用策略；3）记忆管理：分为过程内存、工件内存、经验内存三类存储结构，适配不同的读取与更新触发逻辑；4）规划模块：包含「评估目标定义」与「证据采集路径规划」两层能力，支撑动态调整评测流程
- 梳理了Agent评委在数学、代码、事实校验、医疗、金融、法律等10+领域的落地案例，总结了成本、可靠性、安全、隐私四大落地挑战

### 关键实验
整理并复现了5个主流Agent评委在RewardBench、RM-Bench、JudgeBench三个通用评测基准上的表现：1）仅TIR-Judge在RM-Bench上明显超过非Agent式推理奖励模型，其余Agent评委表现弱于强基线；2）在JudgeBench上，强非Agent式奖励模型与最优Agent评委表现相当，Agent特性带来的增益在偏好类基准上分布不均，需针对证据获取场景专项优化。

### 核心结论
Agent-as-a-Judge的核心价值不是在固定上下文评测中超过被动LLM评委，而是解决需要主动获取外部证据才能做出可靠判决的长尾评测场景
