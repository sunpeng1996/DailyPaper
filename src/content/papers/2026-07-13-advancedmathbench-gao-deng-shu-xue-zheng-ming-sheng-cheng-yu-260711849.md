---
title: 'AdvancedMathBench: A Benchmark Suite for Advanced Mathematical Proof Generation
  and Verification'
title_zh: AdvancedMathBench：高等数学证明生成与验证基准套件
authors:
- Lingkai Kong
- Zijian Wu
- Yuzhe Gu
- Haiteng Zhao
- Wenyong Huang
- Shuang Sun
- Zhicheng Xiong
- Xiaotian Zhang
- Shuya Zhao
- Yan Wang
affiliations:
- Shanghai AI Laboratory
- Shanghai Jiao Tong University
- MMLab, The Chinese University of Hong Kong
- Great Bay University
arxiv_id: '2607.11849'
url: https://arxiv.org/abs/2607.11849
pdf_url: https://arxiv.org/pdf/2607.11849
published: '2026-07-13'
collected: '2026-07-15'
category: Eval
direction: 大模型高阶数学推理能力评测
tags:
- Benchmark
- Mathematical Reasoning
- Proof Generation
- Proof Verification
- LLM Evaluation
one_liner: 构建覆盖本科到博士难度的高等数学证明生成与验证基准，配套细粒度自动验证管线
practical_value: '- 推理类Agent评测可复用其「不唯最终结果、细粒度拆解推理路径错误」的评估逻辑，适配电商智能客服、选品决策Agent的效果评估，避免漏判逻辑错误但结果正确的坏例

  - 复杂业务场景的benchmark搭建可参考其「难度分层划分+验证任务单独标注」的范式，比如多档位商品推荐的效果评测，可按用户消费层级拆分测试集，单独构建排序结果合理性验证集

  - 若业务涉及数理类内容生成（如教辅商品内容种草、科研类用户搜索Query理解），可使用该基准筛选数理推理能力达标的基座LLM，降低下游微调成本'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有大模型数学推理评测多聚焦中学、竞赛难度，高等数学领域评测存在明显短板：覆盖学科范围窄，评估粒度粗，仅校验最终答案正确性，无法准确判断推理过程的有效性，难以真实衡量大模型高阶推理能力。
### 方法关键点
1. 构建双基准套件：包含245道本科（UG）到博士资格考试（QE）难度题目的证明生成基准ProverBench，及888条带专家标注的模型生成证明轨迹构成的证明验证基准VerifierBench；
2. 配套基于大规模专家标注训练的自动验证管线，可输出证明正确性判定及细粒度错误类型评估，与人类专家判断一致性高。
### 关键结果
前沿大模型在该基准上挑战较大：最佳模型GPT-5.5-xhigh在UG、QE难度证明生成任务得分仅64.5、48.9，证明验证任务最佳平衡F1仅65.1，错误检测能力是当前核心瓶颈。
