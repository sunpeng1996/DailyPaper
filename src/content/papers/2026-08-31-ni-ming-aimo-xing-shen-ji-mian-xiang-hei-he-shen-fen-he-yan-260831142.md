---
title: 'Auditing Anonymous AI Models: A Four-Stage Protocol for Black-Box Identity
  Verification'
title_zh: 匿名AI模型审计：面向黑盒身份核验的四阶段协议
authors:
- Yisen Xi
affiliations:
- Independent Researcher, Beijing, China
arxiv_id: '2608.31142'
url: https://arxiv.org/abs/2608.31142
pdf_url: https://arxiv.org/pdf/2608.31142
published: '2026-08-31'
collected: '2026-09-02'
category: LLM
direction: 大模型黑盒身份核验 · AI供应链风险管控
tags:
- Black-box Auditing
- Tokenizer Fingerprinting
- AI Supply Chain
- Model Verification
- Digital Forensics
one_liner: 提出四阶段黑盒审计协议，可匿名核验API服务大模型的所属家族与版本线
practical_value: '- 可复用四阶段黑盒指纹方法，核验第三方大模型API的真实身份，规避AI供应链风险，比如调用匿名模型做生成式推荐时提前确认合规性

  - tokenizer跨长度差分验证的trick可直接复用，在调用多厂商LLM服务时做身份校验，避免服务商偷偷替换低性能模型导致推荐/Agent效果下降

  - 快照溯源配置漂移的思路可用于大模型服务监控，上线后定期比对上下文长度、输出上限等配置变化，避免LLM服务迭代导致的推荐文案生成、Agent推理效果波动'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
2025-2026年大量前沿大模型匿名上线API平台，现有黑盒身份核验方法无准确性验证、模型自报身份不可信，用户无法判断数据合规性、供应链风险与模型能力边界

### 方法关键点
四阶段API模型审计协议流程为：Stage 0 基于互联网档案快照还原模型发布时配置，识别预览/生产版本漂移；Stage 1 基于上下文窗口、输出上限、推理能力、模态属性做配置指纹匹配；Stage 2 用跨长度差分法做tokenizer身份校验，排除短提示碰撞；Stage 3 通过行为探针交叉验证

### 关键结果数字
10个已知身份模型测试：7个完全匹配、2个精度差异、1个部分匹配、0个反向错误；匿名旗舰案例测试准确识别为GLM-5.3版本线，与官方发布结果一致；3个仅需Stage 0的案例中仅输出分级假设或拒绝猜测，无乱猜情况；同步提供仅依赖标准库的实现代码
