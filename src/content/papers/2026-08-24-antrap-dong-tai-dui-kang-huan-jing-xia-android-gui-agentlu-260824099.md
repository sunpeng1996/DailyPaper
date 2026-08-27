---
title: 'Are Android GUI Agents Robust Against Runtime Anomalies? AnTrap: Evaluating
  Agents in Dynamic Adversarial Environments'
title_zh: AnTrap：动态对抗环境下Android GUI Agent鲁棒性评估基准
authors:
- Guo Gan
- Yilun Zhao
- Cong Chen
- Jinbiao Wei
- Tingyu Song
- Zheyuan Yang
- Lin Fu
- Hong Zhou
affiliations:
- Zhejiang University
- Yale University
- Tongji University
- University of Chinese Academy of Sciences
arxiv_id: '2608.24099'
url: https://arxiv.org/abs/2608.24099
pdf_url: https://arxiv.org/pdf/2608.24099
published: '2026-08-24'
collected: '2026-08-27'
category: Agent
direction: GUI Agent 鲁棒性评估与异常分类
tags:
- GUI Agent
- Robustness Evaluation
- Runtime Anomaly
- Adversarial Benchmark
- GRPO
one_liner: 提出分层运行时异常分类体系与AnTrap基准，揭示GUI Agent普遍脆弱性，区分可学习与推理瓶颈类异常
practical_value: '- 开发电商APP智能导购、自动运营等移动端交互Agent时，可复用STAR四层异常分类体系做上线前鲁棒性测试，覆盖弹窗、跳转、动作错误、长序列死锁等真实场景异常，避免上线后失效

  - 做Agent对抗训练时，可借鉴动态异常注入方案，针对State/Action层单步异常用GRPO做针对性训练，可快速提升8%~11%的鲁棒性，无需全量堆训练数据

  - 评估Agent性能时不能只测干净环境，需加入随机异常注入；Round层多步上下文异常无法通过单纯RL解决，需额外增加自校验、轨迹回溯机制优化'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有GUI Agent基准均在干净稳定环境下评估，而真实部署中Agent会遇到大量运行时异常（外部弹窗、应用跳转，内部视觉幻觉、动作错误等），缺乏系统性的鲁棒性评估方案，导致上线后性能骤降。

### 方法关键点
- 提出STAR四层异常分类体系，覆盖State（弹窗、视觉遮挡2类）、Thinking（时序冲突、视觉幻觉2类）、Action（grounding错误、动作类型不匹配等3类）、Round（死锁、上下文断裂、循环3类）共10个细分类别，覆盖绝大多数真实场景异常
- 构建AnTrap基准，基于AndroidWorld扩展到236个支持动态异常注入的任务，注入时保证任务可解，性能下降完全由Agent鲁棒性不足导致，支持异常类型、注入时机、频率灵活配置
- 通过在干净/异常环境下分别做GRPO训练，区分可通过环境学习解决的异常和推理瓶颈类异常

### 关键实验结果
评估16个主流GUI模型（含Claude-Sonnet-4.6、GPT-5.4等闭源模型，GUI-Owl、Qwen3-VL等开源模型），核心结果：
1. 所有模型在异常环境下性能普遍下降，最强的Claude-Sonnet-4.6从干净环境74.2%的成功率降到66.5%，降幅超7个百分点
2. State/Action层单步异常可通过对抗GRPO训练提升8.1%~11%的成功率，但Round层多步上下文异常最多提升不足3%，几乎无法通过单纯RL解决
3. 带Thinking机制的模型在干净环境性能更高，但鲁棒性没有优势，降幅与普通Instruct模型相当

**最值得记住的一句话**：现有GUI Agent的鲁棒性普遍不足，单步异常可通过对抗训练优化，长序列上下文异常需要额外的元认知、自监控回溯机制才能解决
