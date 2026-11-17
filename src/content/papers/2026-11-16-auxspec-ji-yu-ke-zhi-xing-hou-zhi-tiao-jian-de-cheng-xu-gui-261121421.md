---
title: 'AuXSpec: Learning to Autoformalize Program Specifications via Executable Postconditions'
title_zh: AuXSpec：基于可执行后置条件的程序规范自动形式化方法
authors:
- Haocheng Wang
- Weixuan Yuan
- Florian Hübler
- Yinya Huang
- Zhijiang Guo
- Sorrachai Yingchareonthawornchai
- Rasmus Kyng
affiliations:
- ETH Zurich
- HKUST(GZ)
- HKUST
- ETH AI Center
arxiv_id: '2611.21421'
url: https://arxiv.org/abs/2611.21421
pdf_url: https://arxiv.org/pdf/2611.21421
published: '2026-11-16'
collected: '2026-11-17'
category: LLM
direction: 程序规范自动形式化 · LLM训练反馈优化
tags:
- LLM
- FormalVerification
- ReinforcementLearning
- RewardEngineering
- CodeGeneration
one_liner: 提出基于可执行后置条件的AuXSpec框架，大幅提升程序规范自动形式化效果
practical_value: '- 可复用「声明式规则→可执行校验规则」的反馈框架，落地到LLM生成推荐文案、流量调控规则的自动校验场景，无需人工标注即可获得低成本奖励信号

  - 专家迭代+可执行奖励的训练范式，可迁移到电商搜索Query改写、商品属性标准化生成的LLM微调任务，低成本扩大训练样本规模

  - 跨域泛化的基准评估思路，可用于不同垂类商品/场景下生成式推荐模型的效果评测，降低分布偏移带来的业务效果损失'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
程序形式化规范是代码正确性验证的核心基础，但人工编写依赖专业知识、效率极低，现有自动形式化模型训练依赖成本极高的显式证明或对应代码一致性证明，缺乏可扩展的低成本反馈信号。
### 方法关键点
1. 提出AuXSpec Lean框架，将声明式后置条件与可执行版本配对：优先通过类型类解析获取，否则单独定义并做等价性证明
2. 用测试用例执行结果的一致性作为RL奖励信号训练生成模型
3. 合成3037道LeetCode问题样本，通过专家迭代扩展到19.5K Codeforces训练样本
### 关键结果
微调Qwen3.5-9B、Qwen3.8-27B后，AuXSpec-Test基准pass@4分别提升至82.7%、84.3%；跨域Verina基准pass@1最高达84.5%，远超此前开源SOTA的47.6%
