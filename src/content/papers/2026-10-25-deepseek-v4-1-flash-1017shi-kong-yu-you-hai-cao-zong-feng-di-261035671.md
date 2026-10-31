---
title: Evaluating DeepSeek V4.1 Flash-1017 for loss of control and harmful manipulation
  risks
title_zh: DeepSeek V4.1 Flash-1017失控与有害操纵风险第三方评估
authors:
- Yao Huang
- Zhiyuan Zeng
- Yu Wang
- Zhitong Zhu
- Dingcheng Duan
- Hao Li
- Shangzhi Xu
- Yifan Wang
- Jinzhe Tu
- Shukun Xiong
affiliations:
- Fangcun AI Evaluation Team
arxiv_id: '2610.35671'
url: https://arxiv.org/abs/2610.35671
pdf_url: https://arxiv.org/pdf/2610.35671
published: '2026-10-25'
collected: '2026-10-31'
category: Eval
direction: 大模型安全 · 第三方风险评估
tags:
- LLM Safety
- Risk Evaluation
- DeepSeek
- Autonomous Agent
- Open-weight LLM
one_liner: 针对DeepSeek V4.1 Flash-1017开展独立第三方安全评估，对比主流模型给出安全结论与落地建议
practical_value: '- 落地Agent系统（如电商智能导购、运营自动化Agent）时，不能仅校验最终输出，需增加推理轨迹、动作日志的全流程可观测性，及时拦截失控风险

  - 迭代LLM相关业务（如生成式推荐文案、个性化Query改写）时，需将安全评估纳入每一次小版本发布流程，避免安全能力退化

  - 内部评估LLM/Agent业务效果时，除公开基准外需构建私有专属benchmark，规避数据污染导致的评估失真问题'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前开源大模型的前沿安全风险受关注度远低于闭源模型，DeepSeek V4.1 Flash-1017具备强Agent能力，上线首周即成为Open-Router最常用模型，累计处理33.6万亿token，亟需独立第三方安全评估。
### 方法关键点
遵循欧盟通用AI实践准则与AEF-1标准，覆盖评估完整性、失控风险、有害操纵3大维度，共测试34个基准（含5个自研私有基准），与DeepSeek V4系列、GPT-6 Astra、Gemini 3.8 Flash等7款主流闭源/开源模型横向对比。
### 关键结果数字
- 相比V4世代安全性能大幅提升，多维度接近/持平头部闭源模型，但仍存在需重点关注的风险行为
- 输出3项可落地的行业通用安全建议：小版本迭代内嵌安全评估、全流程观测替代仅终态校验、私有基准补充公开评估
