---
title: 'ToolHazard: Scaling Adversarial Environments for Security Evaluation and Alignment
  of LLM-based Agents'
title_zh: ToolHazard：面向LLM Agent安全评测与对齐的可扩展对抗环境生成框架
authors:
- Yutao Mou
- Pengfei Yang
- Zhe Yin
- Zhangchi Xue
- Xiaotian Luan
- Dingyao Yu
- Tong Zhang
- Shikun Zhang
- Wei Ye
affiliations:
- 北京大学软件工程国家工程研究中心
- 腾讯微信AI
- 哈尔滨工业大学
- 北京邮电大学
arxiv_id: '2608.11878'
url: https://arxiv.org/abs/2608.11878
pdf_url: https://arxiv.org/pdf/2608.11878
published: '2026-08-11'
collected: '2026-08-13'
category: Agent
direction: Agent安全 · 对抗环境自动生成
tags:
- LLM Agent
- Prompt Injection
- Security Evaluation
- Adversarial Training
- Benchmark
one_liner: 提出可自动合成有状态对抗环境的框架，配套评测基准与对齐数据集，强化Agent抗注入鲁棒性
practical_value: '- 电商/广告场景Agent部署可复用本文防御结论：优先采用JSON/YAML等结构化工具输出格式，降低prompt注入风险；对执行链路前几步的工具返回、返回内容末尾字段做重点恶意检测

  - 业务侧做Agent安全评测可复用ToolHazard三元组框架：环境模拟器自动生成业务场景下的工具交互环境，攻击Agent自动发现潜在注入点，用户模拟器生成长链路任务，低成本扩展安全测试用例

  - 面向Agent的安全对齐可复用其SFT+RL流程：用干净环境的正常轨迹做SFT保障业务效用，用对抗环境的轨迹做GRPO强化学习惩罚被劫持行为，可在几乎不损失正常任务成功率的前提下降低攻击成功率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent安全评测依赖人工构造环境、预定义注入点，可扩展性差，无法覆盖复杂业务场景下的未知注入风险；且现有攻击模拟多为随机或固定模式，无法真实还原环境侧间接prompt注入的实际攻击路径，导致Agent安全评测和对齐的泛化性不足，难以支撑生产级Agent的安全落地。

### 方法关键点
- 核心框架分为3模块：Environment Simulator基于种子任务自动生成可执行、有状态的工具交互环境，经双Agent校验确保逻辑正确性；User Simulator基于生成环境自动构造长链路用户任务；Attacker Agent自动发现环境可注入点，生成场景专属攻击载荷，模拟环境侧prompt注入
- 配套ToolHazard-Bench评测基准：覆盖28个领域、87个长链路任务（平均15.56执行步）、512个工具，复杂度远高于现有同类基准
- 配套ToolHazard-Align对齐数据集：含60个领域的1040条训练样本，支持SFT+RL的安全对齐流程，奖励函数同时激励正常任务完成、惩罚被注入劫持的行为

### 关键实验结果
在7款主流LLM Agent上测试，现有模型普遍存在高漏洞率，例如DeepSeek-V3.2的工具选择类攻击成功率达73.33%；注入时机越早、注入位置越靠近返回内容末尾，攻击成功率越高（最早注入比随机注入ASR高20pct以上）；经ToolHazard-Align对齐的Qwen3-8B，在ToolHazard-Bench上ASR从36.10%降至18.06%，在第三方基准AgentDojo上ASR从29.16%降至18.34%，同时正常任务成功率提升8.3pct。

**最值得记住的结论**：LLM Agent的环境侧prompt注入风险远高于预期，通过可扩展对抗环境生成+针对性对齐的方案，可在几乎不损失业务效用的前提下大幅提升Agent鲁棒性。
