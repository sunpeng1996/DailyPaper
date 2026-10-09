---
title: 'A Closer Look at Agentic BBO: Benchmarking LLM Agents for Black-Box Optimization'
title_zh: Agentic BBO深度解析：面向黑盒优化的LLM Agent基准测试
authors:
- Ming Chen
- Rong-Xi Tan
- Ke Xue
- Yu-Jie Zhou
- Taiye Lu
- Zhi-Xuan Gao
- Peng Xie
- Zijun Shen
- Chen Lu
- Haopu Shang
affiliations:
- 南京大学计算机软件新技术国家重点实验室
- 南京大学人工智能学院
arxiv_id: '2610.12183'
url: https://arxiv.org/abs/2610.12183
pdf_url: https://arxiv.org/pdf/2610.12183
published: '2026-10-07'
collected: '2026-10-09'
category: Agent
direction: LLM Agent · 黑盒优化基准测试
tags:
- LLM Agent
- Black-Box Optimization
- Benchmark
- Hyperparameter Optimization
- Bayesian Optimization
one_liner: 推出跨5领域的AgenticBBO-Bench基准，系统分析LLM Agent黑盒优化的性能影响因素
practical_value: '- 做推荐系统超参调优、召回/排序策略黑盒优化时，可优先让Agent基于任务语义自定义分析逻辑，而非强制绑定预置数值优化工具，实测后者无稳定收益

  - 给优化类Agent输入先验知识时，优先保证先验的正确性与可落地性，通用任务语义的收益比模糊的领域先验更稳定，错误先验甚至会降低性能

  - 优化类Agent可采用「LLM Agent预热探索+数值优化器后续迭代」的混合架构，既保留Agent挖掘语义信息的优势，又能降低长期调用大模型的token成本

  - 选型大模型时不要盲目追求高价旗舰款，实测DeepSeek V4.1 Flash与GPT-6 Astra优化性能接近但成本低数倍，优先做Agent适配而非升级模型'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Agentic BBO（基于LLM Agent的黑盒优化）研究采用的任务域、系统配置差异极大，实验结果无法横向对比，各设计模块的收益也无法独立验证，缺乏跨领域的统一评估基准，阻碍了该方向的落地应用。
### 方法关键点
- 构建AgenticBBO-Bench跨领域基准，覆盖合成数值函数优化、超参优化、数据库调优、芯片布局、分子设计5大领域，支持连续、混合、离散结构化等多种搜索空间，统一有限预算评估协议
- 通过受控实验拆解三大核心影响因素：可调用的优化工具集合、任务信息与先验知识、LLM在优化链路中的参与程度
- 设计5任务前沿挑战，采用统一协议测试多款前沿大模型的优化性能与token成本
### 关键结果
对比直接LLM生成、主流数值优化器（GP-BO、TuRBO、CMA-ES等），Agentic BBO在5个领域平均性能比直接LLM优化高30.3%，在4个领域超过最优数值优化器；7款前沿大模型测试中，GPT-6 Astra得分59.1、DeepSeek V4.1 Flash得分58.4，二者性能接近但后者token成本低数倍，处于性能-成本帕累托前沿。
### 核心结论
Agentic BBO的核心优势是利用任务语义构建自定义搜索策略，而非单纯依赖预置的数值优化工具。
