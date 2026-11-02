---
title: 'When Requirements Interact: Scaling Long-Horizon Coding via Interdependent
  Specifications'
title_zh: CodeSpecWeave：面向长周期编码的多约束耦合任务合成框架
authors:
- Yishuo Cai
- Minzheng Wang
- Liang Zhao
- Linghao Zhang
- Lei Li
- Shicheng Li
- Xu Sun
- Fuli Luo
affiliations:
- 小米LLM Core
- 北京大学
- 香港大学
arxiv_id: '2610.40256'
url: https://arxiv.org/abs/2610.40256
pdf_url: https://arxiv.org/pdf/2610.40256
published: '2026-10-28'
collected: '2026-11-02'
category: Agent
direction: 编码Agent · 多约束任务合成与能力强化
tags:
- CodingAgent
- LongHorizonTask
- TaskSynthesis
- ReinforcementLearning
- LLMBenchmark
one_liner: 提出耦合多约束的编码任务合成框架，配套训练集与基准，强化编码Agent复杂约束处理能力
practical_value: '- 构建业务复杂规则类Agent（如商品合规校验、营销活动叠加规则执行Agent）的训练数据时，可复用「多约束耦合设计+多模型轨迹校验」pipeline，避免训练任务退化为独立规则检查清单，强制Agent学会联合推理业务规则（如商品上线需同时满足合规、定价、库存、展示逻辑）。

  - Agent业务评测集构建可借鉴双Agent校验逻辑：先由合成Agent生成约束和测试用例，再由评审Agent基于多个模型的求解轨迹过滤FP/FN用例，大幅提升评测集可靠性，适合电商复杂运营任务的Agent评测。

  - 训练处理多约束的Agent时，优先引入耦合约束的训练任务做RL训练，论文显示这类任务对长周期复杂任务的性能提升远高于普通独立约束任务，可迁移至大促多活动叠加规则处理、订单履约多节点校验等场景的Agent优化。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有长周期编码Agent的训练任务普遍约束密度低、规则独立，无法模拟真实场景中多规则耦合的复杂需求（如代码修改需同时满足接口兼容、异常处理、状态一致性等要求），导致训练出的Agent落地时易顾此失彼；同时复杂耦合约束的任务合成存在两大痛点：单纯加约束易退化为独立检查清单，测试校验易漏判隐藏问题或误杀合法解。
### 方法关键点
- 基于真实开发者提交的规则种子，由合成Agent迭代生成耦合的任务需求与可执行测试用例，确保单个需求的实现选择会约束其他需求的可行解，强制Agent联合推理；
- 引入双Agent校验流程：多个求解Agent生成任务执行轨迹与补丁，评审Agent基于轨迹修复测试的FP/FN问题，确保测试可靠性；
- 构建含4670个训练任务的数据集，以及含100个高标注质量任务、1044个耦合约束的基准测试集CodeSpecWeave-Bench。
### 关键实验
对比SWE-PI、MiMo Coding等训练数据集，用CodeSpecWeave任务做RL训练后，MiMo-V2.6-Flash-SFT在DeepSWE-v1.1上准确率从54.42%提升至62.98%，在CodeSpecWeave-Bench上准确率从59%提升至70.67%，平均在4个编码基准上领先所有基线；当前最强模型GPT-6 Astra在该基准上通过率仅74%，耦合约束处理仍有较大优化空间。
> 值得记住的结论：处理多约束的长周期任务，核心是让Agent学会联合推理耦合约束，而非逐一满足独立规则。
