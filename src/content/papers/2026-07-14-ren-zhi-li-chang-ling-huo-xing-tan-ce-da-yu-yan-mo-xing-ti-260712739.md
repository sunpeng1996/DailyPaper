---
title: 'Epistemic Stance Flexibility Probing: Measuring Prompt-Conditioned Register
  Shift in Large Language Models'
title_zh: 认知立场灵活性探测：大语言模型提示条件下的语域迁移度量
authors:
- Binwen Liu
- Yilin Ren
arxiv_id: '2607.12739'
url: https://arxiv.org/abs/2607.12739
pdf_url: https://arxiv.org/pdf/2607.12739
published: '2026-07-14'
collected: '2026-07-15'
category: Eval
direction: 大语言模型评估 · 认知立场探测
tags:
- LLM Evaluation
- Epistemic Stance
- Prompt Conditioning
- Behavioral Benchmark
- Register Shift
one_liner: ESFP行为基准，可度量大模型在外部/自我归因提示下的认知立场切换能力
practical_value: '- 对话式导购Agent开发中，可复用该基准的测试逻辑，验证Agent区分「转述商品参数/专家观点」「表达自身推荐立场」的边界能力，避免导购话术误导用户

  - 优化Agent回复prompt时，可参考四类评估维度（词汇归因、角色响应、立场密度、跨条件一致性）校准不同场景下的话术风格切换效果

  - 大模型选型时可补充该维度测试，无需盲目追求大参数量/推理优化模型，部分中小参数模型立场切换能力不亚于头部闭源模型'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有LLM准确率、指令跟随、安全类基准均无法评估模型认知语域切换能力：即请求转述第三方争议观点时保持中立，请求表达自身观点时明确表态，这是可信对话Agent的核心能力但缺乏度量方案。
### 方法关键点
ESFP行为基准包含104个受控样本，覆盖6类认知场景、5种措辞模板，从4个互补维度评估：词汇层面自我归因、表征层对角色框架的响应度、LLM评审团评估的句子级立场内容密度、跨条件立场一致性。
### 关键结果
测试5家厂商的8个前沿模型，发现认知灵活性与通用模型能力基本正交：27B开源模型表现匹配头部闭源系统，同系列旗舰模型表现弱于轻量版本，推理优化模型未展现出更高灵活性；立场内容密度是最强评估信号，「I think」等表层词汇标记变化不必然对应实际立场变化。
